from pathlib import Path
from birdnet import predict_species_within_audio_file, SpeciesPredictions

def main(audio_file):
    raw = predict_species_within_audio_file(Path(audio_file))
    preds = SpeciesPredictions(raw)
    interval = (0.0, 3.0)
    top = sorted(preds[interval].items(), key=lambda x: -x[1])[:3]
    for species, confidence in top:
        print(f"{interval[0]:.1f}–{interval[1]:.1f}s: {species} ({confidence:.2f})")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python infer_bird.py <path/to/audio.wav>")
        sys.exit(1)
    main(sys.argv[1])

