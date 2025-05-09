# audio_server.py

import socketserver
import struct
import time
import os

SAVE_DIR = "received_clips"
os.makedirs(SAVE_DIR, exist_ok=True)

class AudioTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Read exactly 4 bytes for length
        raw = self.request.recv(4)
        if len(raw) < 4:
            return
        (length,) = struct.unpack('!I', raw)

        # Read the WAV data
        data = b''
        while len(data) < length:
            packet = self.request.recv(length - len(data))
            if not packet:
                break
            data += packet

        # Save with timestamp
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename  = os.path.join(SAVE_DIR, f"clip_{timestamp}.wav")
        with open(filename, 'wb') as f:
            f.write(data)
        print(f"Saved clip to {filename} ({length} bytes)")

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9998
    with socketserver.TCPServer((HOST, PORT), AudioTCPHandler) as srv:
        print(f"Audio server listening on {HOST}:{PORT}")
        srv.serve_forever()

