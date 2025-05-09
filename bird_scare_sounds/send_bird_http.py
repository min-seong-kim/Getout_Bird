# send_bird_http.py
import requests

# ngrok 또는 고정 서버 주소
LOCAL_PC_URL = "https://7977-61-98-214-248.ngrok-free.app"

def send_detected_bird(bird_name):
    try:
        res = requests.post(
            f"{LOCAL_PC_URL}/bird",
            json={"species": bird_name},
            timeout=5
        )
        print(f"[전송 완료] '{bird_name}' → 응답: {res.status_code} {res.text}")
    except Exception as e:
        print(f"[전송 실패] {e}")

# 예시 호출
if __name__ == "__main__":
    send_detected_bird("참새")

