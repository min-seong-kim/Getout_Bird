#!/usr/bin/env python3
import time
from pathlib import Path
from birdnet import predict_species_within_audio_file, SpeciesPredictions

def get_latest_wav(directory: Path) -> Path | None:
    wav_files = list(directory.glob("*.wav"))
    return max(wav_files, key=lambda f: f.stat().st_mtime) if wav_files else None

def run_inference(wav_path: Path) -> None:
    raw = predict_species_within_audio_file(wav_path)
    preds = SpeciesPredictions(raw)
    interval = (0.0, 3.0)
    top3 = sorted(preds[interval].items(), key=lambda x: -x[1])[:3]

    print(f"=== {wav_path.name} ===")
    for species, conf in top3:
        print(f"{interval[0]:.1f}-{interval[1]:.1f}s → {species}: {conf:.2f}")
    print()

def main():
    clips_dir = Path("../received_clips")
    last_processed: Path | None = None

    while True:
        latest = get_latest_wav(clips_dir)
        if latest and latest != last_processed:
            run_inference(latest)
            last_processed = latest
        time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

