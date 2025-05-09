import os
import random
import time
import subprocess
import logging

# 로깅 설정
logging.basicConfig(
    filename="bird_sound_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# 새 종류별 사운드 매핑
bird_sound_map = {
    "멧비둘기": [
        "sounds/dove_tone_4kHz.wav",
        "sounds/dove_tone_5kHz.wav",
        "sounds/dove_tone_6kHz.wav",
        "sounds/eagle_2sec.wav"
    ],
    "참새": [
        "sounds/sparrow_tone_6kHz.wav",
        "sounds/magpie_tone_8kHz.wav",
        "sounds/sparrow_tone_9kHz.wav",
        "sounds/eagle_2sec.wav",
        "sounds/magpie_tone_10kHz.wav"
    ],
    "까치": [
        "sounds/magpie_tone_8kHz.wav",
        "sounds/crow_tone_9kHz.wav",
        "sounds/magpie_tone_10kHz.wav",
        "sounds/crow_tone_11kHz.wav",
        "sounds/magpie_tone_12kHz.wav",
        "sounds/eagle_2sec.wav",
        "sounds/tiger_roar_4sec.wav"
    ],
    "까마귀": [
        "sounds/crow_tone_9kHz.wav",
        "sounds/crow_tone_11kHz.wav",
        "sounds/crow_tone_12kHz.wav",
        "sounds/tiger_roar_4sec.wav",
        "sounds/eagle_2sec.wav"
    ]
}


# 사운드 재생 함수
def play_sound(file_path):
    if not os.path.exists(file_path):
        msg = f"[X] 파일이 존재하지 않습니다: {file_path}"
        print(msg)
        logging.error(msg)
        return

    try:
        if file_path.endswith(".mp3"):
            subprocess.run(["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", file_path], check=True)
        elif file_path.endswith(".wav"):
            powershell_cmd = f"(New-Object Media.SoundPlayer '{file_path}').PlaySync();"
            subprocess.run(["powershell", "-Command", powershell_cmd], check=True)
        else:
            msg = f"[X] 지원되지 않는 파일 형식: {file_path}"
            print(msg)
            logging.error(msg)
    except subprocess.CalledProcessError as e:
        msg = f"[X] 사운드 재생 중 오류 발생: {e}"
        print(msg)
        logging.error(msg)


# 새별 특성 기반 재생 패턴
def play_sparrow(sounds):
    print("  🔀 참새: 고주파 빠른 셔플 재생")
    logging.info("참새: 고주파 빠른 셔플 재생")
    for s in random.sample(sounds, len(sounds)):
        play_sound(s)
        time.sleep(0.3)


def play_crow(sounds):
    print(" 까마귀: 랜덤 + 불규칙 재생")
    logging.info("까마귀: 랜덤 + 불규칙 재생")
    repeat_count = random.randint(3, 6)
    for _ in range(repeat_count):
        s = random.choice(sounds)
        play_sound(s)
        time.sleep(random.uniform(0.2, 1.2))
        if random.random() < 0.3:
            play_sound(s)
            time.sleep(random.uniform(0.1, 0.5))


def play_magpie(sounds):
    print(" 까치: 점진적 딜레이 재생")
    logging.info("까치: 점진적 딜레이 재생")
    delay = 0.3
    for s in sounds:
        play_sound(s)
        time.sleep(delay)
        delay += 0.2


def play_dove(sounds):
    print(" 멧비둘기: 반복 재생")
    logging.info("멧비둘기: 반복 재생")
    for _ in range(2):
        for s in sounds:
            play_sound(s)
            time.sleep(0.2)


# 메인 함수
def play_bird_defense(bird_type):
    sounds = bird_sound_map.get(bird_type)

    if not sounds:
        msg = f"[X] '{bird_type}' 에 대한 사운드가 없습니다."
        print(msg)
        logging.error(msg)
        return

    msg = f"[{bird_type}] 퇴치 사운드 시작"
    print(msg)
    logging.info(msg)

    # 새별 재생 분기
    if bird_type == "참새":
        play_sparrow(sounds)
    elif bird_type == "까마귀":
        play_crow(sounds)
    elif bird_type == "까치":
        play_magpie(sounds)
    elif bird_type == "멧비둘기":
        play_dove(sounds)
    else:
        # 기본 fallback
        print(" 기본 순차 재생")
        logging.info("기본 순차 재생")
        for s in sounds:
            play_sound(s)
            time.sleep(1)
