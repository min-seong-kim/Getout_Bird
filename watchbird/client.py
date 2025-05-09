# 호스트에서 돌려야하는 client.py
import cv2
import socket
import threading
import struct
import time
import datetime

SERVER_IP = "220.149.235.221"  # 서버 IP
SERVER_PORT = 9999            # 서버 포트

# 프레임을 서버로 전송하는 함수
def send_motion_frames():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("카메라를 열 수 없습니다.")
        return

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))
    except Exception as e:
        print(f"서버에 연결할 수 없습니다: {e}")
        cap.release()
        return

    print("서버에 연결되었습니다. 움직임이 감지되면 프레임을 전송합니다.")

    prev_frame = None
    while True:
        ret, frame = cap.read()
        if not ret:
            print("프레임 수신 실패")
            break

        # 프레임 화면에 표시
        try:
            cv2.imshow("Client - Capturing", frame)
        except Exception as e:
            print("cv2.imshow error:", e)

        # 움직임 감지를 위해 회색조로 변환 후 비교
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if prev_frame is None:
            prev_frame = gray
            continue

        delta = cv2.absdiff(prev_frame, gray)
        thresh = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)
        motion_detected = cv2.countNonZero(thresh) > 5000

        if motion_detected:
            print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [Motion] 움직임 감지됨: 프레임 전송")
            # 프레임을 JPEG로 인코딩 후 전송
            _, buffer = cv2.imencode(".jpg", frame)
            data = buffer.tobytes()
            size = len(data)
            try:
                client_socket.sendall(struct.pack("!I", size))
                client_socket.sendall(data)
            except Exception as e:
                print(f"전송 중 오류 발생: {e}")
                break

        prev_frame = gray

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    client_socket.close()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    send_motion_frames()
