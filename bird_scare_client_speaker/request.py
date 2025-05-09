import os
import requests

SAVE_DIR = "/home/getout/workspace/watchbird/save_bird_class"
SERVER_ENDPOINT = "https://62fa-61-98-214-248.ngrok-free.app/bird"  # 혹은 http://localhost:port/bird

def get_latest_prediction_name():
    txt_files = [f for f in os.listdir(SAVE_DIR) if f.endswith(".txt") and f.startswith("frame_")]
    if not txt_files:
        print("❌ 예측 결과 파일이 없습니다.")
        return None

    latest = sorted(txt_files, key=lambda f: int(f.split("_")[1].split(".")[0]), reverse=True)[0]
    with open(os.path.join(SAVE_DIR, latest), "r", encoding="utf-8") as f:
        bird = f.read().strip()
    return bird

def send_to_server(bird_name):
    payload = { "name": bird_name }
    try:
        res = requests.post(SERVER_ENDPOINT, json=payload, timeout=3)
        print(f"✅ 전송 완료: {bird_name}")
        print(f"응답 코드: {res.status_code}")
        print(f"응답 내용: {res.text}")
    except Exception as e:
        print(f"❌ 서버 전송 실패: {e}")

if __name__ == "__main__":
    bird_name = get_latest_prediction_name()
    if bird_name:
        send_to_server(bird_name)
