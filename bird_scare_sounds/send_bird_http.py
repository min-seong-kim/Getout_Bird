# send_detected_bird_socket.py
import requests

# 🔥 여기에 ngrok에서 나온 주소 넣기
LOCAL_PC_URL = "https://9966-211-36-133-203.ngrok-free.app"

def send_bird_to_local(bird_name):
    try:
        res = requests.post(
            f"{LOCAL_PC_URL}/bird",
            json={"species": bird_name},
            timeout=5
        )
        print(f"[🚀 전송 완료] {bird_name} → 응답: {res.status_code} {res.text}")
    except Exception as e:
        print(f"[❌ 전송 실패] {e}")

# 예시
send_bird_to_local("참새")

