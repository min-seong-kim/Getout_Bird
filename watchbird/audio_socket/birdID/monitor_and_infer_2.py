#!/usr/bin/env python3
import time
import json
from pathlib import Path
from birdnet import predict_species_within_audio_file, SpeciesPredictions

# English-to-Korean mapping
_MAPPING = {
    "crow": "까마귀",
    "pigeon": "비둘기",
    "dove": "비둘기",
    "sparrow": "참새",
    "warbler": "까치",
    "magpie": "까치"
}

def get_latest_wav(directory: Path) -> Path | None:
    wav_files = list(directory.glob("*.wav"))
    return max(wav_files, key=lambda f: f.stat().st_mtime) if wav_files else None

def map_species_to_korean(species: str) -> str | None:
    low = species.lower()
    for eng, kor in _MAPPING.items():
        if eng in low:
            return kor
    return None

def run_inference_and_dump_json(wav_path: Path) -> None:
    # 1) Run BirdNET inference on the 0–3s interval
    raw = predict_species_within_audio_file(wav_path)
    preds = SpeciesPredictions(raw)
    interval = (0.0, 3.0)
    
    # 2) Pick top species by confidence
    top_species, _ = max(preds[interval].items(), key=lambda x: x[1])
    
    # 3) Map to Korean name
    kor_name = map_species_to_korean(top_species) or ""
    
    # 4) Dump minimal JSON
    output = {"name": kor_name}
    json_path = wav_path.with_suffix(".json")
    with open(json_path, "w", encoding="utf-8") as jf:
        json.dump(output, jf, ensure_ascii=False)
    
    print(f"Wrote {json_path.name}: {output}")

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

