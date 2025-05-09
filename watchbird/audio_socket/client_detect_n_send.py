# detect_band_socket.py

import sounddevice as sd
import numpy as np
from scipy.signal import butter, lfilter
import threading
import signal
import collections
import wave
import io
import socket
import struct
import time

# ---- 1) Filter design ----
def make_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    return butter(order, [lowcut/nyq, highcut/nyq], btype='band')

def bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = make_bandpass(lowcut, highcut, fs, order=order)
    return lfilter(b, a, data)

# ---- 2) RMS → dBFS ----
def rms_to_dbfs(rms, ref=1.0):
    return -np.inf if rms <= 0 else 20 * np.log10(rms / ref)

# ---- 3) Socket send ----
SERVER_HOST = '220.149.235.221'   # e.g. '192.168.0.10'
SERVER_PORT = 9998

def send_clip_socket(wav_bytes: bytes):
    """Send 4-byte length + wav_bytes to the server."""
    try:
        with socket.create_connection((SERVER_HOST, SERVER_PORT)) as sock:
            # send length prefix (big-endian uint32)
            sock.sendall(struct.pack('!I', len(wav_bytes)))
            sock.sendall(wav_bytes)
        print(f"Sent clip ({len(wav_bytes)} bytes) at {time.strftime('%H:%M:%S')}")
    except Exception as e:
        print(f"Socket send error: {e}")

# ---- 4) Globals & buffers ----
SAMPLE_RATE      = 44100
BLOCK_SIZE       = 1024
BAND_LOW         = 1000
BAND_HIGH        = 6000
DBFS_THRESHOLD   = -30.0
PAST_SECONDS     = 5
FUTURE_SECONDS   = 5

PAST_BLOCKS    = int(np.ceil(PAST_SECONDS * SAMPLE_RATE / BLOCK_SIZE))
FUTURE_FRAMES  = FUTURE_SECONDS * SAMPLE_RATE

past_buffer      = collections.deque(maxlen=PAST_BLOCKS)
recording_future = False
future_frames_left = 0
future_buffer     = []

# ---- 5) Callback ----
def audio_callback(indata, frames, tstamp, status):
    global recording_future, future_frames_left
    if status:
        print(f"Stream status: {status}", flush=True)

    samples = indata[:, 0].copy()
    past_buffer.append(samples)

    if recording_future:
        future_buffer.append(samples)
        future_frames_left -= len(samples)
        if future_frames_left <= 0:
            # assemble WAV
            past = np.concatenate(list(past_buffer))
            future = np.concatenate(future_buffer)
            clip = np.concatenate([past, future])
            # build WAV bytes
            int16_samples = np.int16(clip * 32767)
            bio = io.BytesIO()
            with wave.open(bio, 'wb') as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(SAMPLE_RATE)
                wf.writeframes(int16_samples.tobytes())
            wav_bytes = bio.getvalue()
            # send
            send_clip_socket(wav_bytes)

            # reset
            recording_future = False
            future_buffer.clear()
        return

    # detection path
    filtered = bandpass_filter(samples, BAND_LOW, BAND_HIGH, SAMPLE_RATE)
    rms  = np.sqrt(np.mean(filtered**2))
    dbfs = rms_to_dbfs(rms)
    if dbfs > DBFS_THRESHOLD:
        # find dominant freq
        fft_vals = np.abs(np.fft.rfft(filtered))
        freqs   = np.fft.rfftfreq(len(filtered), 1/SAMPLE_RATE)
        mask    = (freqs>=BAND_LOW)&(freqs<=BAND_HIGH)
        peak = freqs[mask][np.argmax(fft_vals[mask])] if np.any(mask) else np.nan
        print(f"[{tstamp.inputBufferAdcTime:.3f}] Trigger! RMS={rms:.4f}, "
              f"dBFS={dbfs:.1f}, freq≈{peak:.1f}Hz → capturing…", flush=True)
        recording_future   = True
        future_frames_left = FUTURE_FRAMES

# ---- 6) Graceful shutdown ----
stop_event = threading.Event()
def _signal_handler(sig, frame):
    print("\nStopping…", flush=True)
    stop_event.set()

signal.signal(signal.SIGINT, _signal_handler)

# ---- 7) Main ----
if __name__ == "__main__":
    print("Starting. Ctrl+C to stop.")
    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        blocksize=BLOCK_SIZE,
        channels=1,
        callback=audio_callback
    ):
        stop_event.wait()
    print("Exited.")

