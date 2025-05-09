# bird_sound_player.py
import subprocess
import random
import time
import os

# 새 종류별 사운드 매핑 (sounds/ 디렉토리 기준)
bird_sound_map = {
    "멧비둘기": [
        "sounds/dove_tone_4kHz.wav",
        "sounds/dove_tone_5kHz.wav",
        "sounds/dove_tone_6kHz.wav",
        "sounds/eagle_2sec.mp3"
    ],
    "참새": [
        "sounds/sparrow_tone_6kHz.wav",
        "sounds/sparrow_tone_9kHz.wav",
        "sounds/eagle_2sec.mp3",
        "sounds/magpie_tone_10kHz.wav"
    ],
    "까치": [
        "sounds/magpie_tone_8kHz.wav",
        "sounds/magpie_tone_10kHz.wav",
        "sounds/magpie_tone_12kHz.wav",
        "sounds/eagle_2sec.mp3",
        "sounds/tiger_roar_4sec.mp3"
    ],
    "까마귀": [
        "sounds/crow_tone_9kHz.wav",
        "sounds/crow_tone_11kHz.wav",
        "sounds/crow_tone_12kHz.wav",
        "sounds/tiger_roar_4sec.mp3",
        "sounds/eagle_2sec.mp3"
    ]
}

def play_sound_ffplay(file_path):
    subprocess.run([
        "ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", file_path
    ])

def play_bird_defense(bird_type, mode="sequence"):
    sounds = bird_sound_map.get(bird_type)
    if not sounds:
        print(f"[X] '{bird_type}' 에 대한 사운드가 없습니다.")
        return

    print(f"[{bird_type}] 퇴치 사운드 시작 (모드: {mode})")

    if mode == "random":
        s = random.choice(sounds)
        print(f"  🔊 재생: {os.path.basename(s)}")
        play_sound_ffplay(s)
    elif mode == "sequence":
        for s in sounds:
            print(f"  🔊 재생: {os.path.basename(s)}")
            play_sound_ffplay(s)
            time.sleep(1)
    else:
        print(f"[X] 알 수 없는 모드: {mode}")

