import requests

# ngrok으로 연결된 로컬 listener 주소
NGROK_URL = "https://62fa-61-98-214-248.ngrok-free.app"

# 테스트용 조류 종류 (시스템에서 지원하는 이름만 사용해야 함)
bird = "까마귀"

# 최소 요청 payload
payload = {
    "name": bird
}

try:
    res = requests.post(f"{NGROK_URL}/bird", json=payload, timeout=3)
    print(f"[서버] 응답 코드: {res.status_code}")
    print(f"[서버] 응답 내용: {res.text}")
except Exception as e:
    print(f"[서버] 요청 실패: {e}")

