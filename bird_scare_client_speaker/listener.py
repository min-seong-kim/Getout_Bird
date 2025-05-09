from flask import Flask, request
from bird_sound_player import play_bird_defense
import threading
import requests

app = Flask(__name__)

def play_and_callback(bird, callback_url):
    play_bird_defense(bird)
    print(f"[완료] '{bird}' 사운드 출력 완료")

    if callback_url:
        try:
            res = requests.post(callback_url, json={"status": "done", "bird": bird}, timeout=3)
            print(f"[ 콜백 전송 완료] {callback_url} → {res.status_code}")
        except Exception as e:
            print(f"[ 콜백 실패] {e}")

@app.route("/ping", methods=["GET"])
def ping():
    print("[PING 요청 수신]")
    return "pong", 200

@app.route("/bird", methods=["POST"])
def handle_bird():
    data = request.json
    bird = data.get("species")
    callback_url = data.get("callback")

    if not bird:
        print("[오류] species 없음")
        return "Invalid request", 400

    print(f"[수신] '{bird}' 감지됨 → 사운드 출력 (비동기)")
    
    #  백그라운드에서 실행
    threading.Thread(target=play_and_callback, args=(bird, callback_url)).start()

    return "Sound playback started", 200  #  응답을 먼저 줌

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7777)