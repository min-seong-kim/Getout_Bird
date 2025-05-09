import socket
import cv2
import numpy as np
import time

HOST = ''  # 서버 IP (빈 문자열이면 모든 인터페이스)
PORT = 9999
MIN_AREA = 5000  # 움직임 감지 기준 최소 면적
FRAME_INTERVAL = 1.0  # 초 단위로 프레임 처리 간격

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"서버 시작. 포트 {PORT}에서 클라이언트 연결 대기 중...")

conn, addr = server_socket.accept()
print(f"클라이언트 연결됨: {addr}")

prev_frame = None
data = b""
payload_size = 4

while True:
    # 프레임 길이 수신
    while len(data) < payload_size:
        packet = conn.recv(4096)
        if not packet:
            break
        data += packet
    if len(data) < payload_size:
        break
    frame_size = int.from_bytes(data[:4], byteorder='big')
    data = data[4:]

    # 실제 프레임 수신
    while len(data) < frame_size:
        data += conn.recv(4096)
    frame_data = data[:frame_size]
    data = data[frame_size:]

    frame = cv2.imdecode(np.frombuffer(frame_data, np.uint8), cv2.IMREAD_COLOR)
    if frame is None:
        continue

    # 흑백 변환 및 블러 적용
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # 첫 프레임 저장
    if prev_frame is None:
        prev_frame = gray
        continue

    # 프레임 차이 계산
    frame_delta = cv2.absdiff(prev_frame, gray)
    thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    motion_detected = any(cv2.contourArea(c) > MIN_AREA for c in contours)
    if motion_detected:
        timestamp = int(time.time())
        filename = f"frame_{timestamp}.jpg"
        save_path = f"/home/getout/workspace/watchbird/save/{filename}"
        cv2.imwrite(save_path, frame)
        print(f"움직임 감지됨! 프레임 저장됨: {save_path}")

    prev_frame = gray

conn.close()
server_socket.close()

