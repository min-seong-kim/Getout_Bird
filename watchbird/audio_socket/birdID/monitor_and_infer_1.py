#!/usr/bin/env python3
import time
import json
from pathlib import Path
from birdnet import predict_species_within_audio_file, SpeciesPredictions

def get_latest_wav(directory: Path) -> Path | None:
    wav_files = list(directory.glob("*.wav"))
    return max(wav_files, key=lambda f: f.stat().st_mtime) if wav_files else None

def run_inference_and_dump_json(wav_path: Path) -> None:
    # run BirdNET inference
    raw = predict_species_within_audio_file(wav_path)
    preds = SpeciesPredictions(raw)
    interval = (0.0, 3.0)
    top3 = sorted(preds[interval].items(), key=lambda x: -x[1])[:3]

    # prepare JSON structure
    output = {
        "file": wav_path.name,
        "interval": {"start_sec": interval[0], "end_sec": interval[1]},
        "predictions": [
            {"species": species, "confidence": float(conf)}
            for species, conf in top3
        ]
    }

    # write to .json next to the .wav
    json_path = wav_path.with_suffix('.json')
    with open(json_path, 'w', encoding='utf-8') as jf:
        json.dump(output, jf, ensure_ascii=False, indent=2)

    print(f"Wrote results to {json_path.name}")

def main():
    clips_dir = Path("../received_clips")
    last_processed: Path | None = None

    while True:
        latest = get_latest_wav(clips_dir)
        if latest and latest != last_processed:
            run_inference_and_dump_json(latest)
            last_processed = latest
        time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

