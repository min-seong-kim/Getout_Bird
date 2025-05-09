from inference_sdk import InferenceHTTPClient
import cv2
import json

# 클라이언트 생성
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="7Qu9IPVAZ7FNTC49jwAT"
)

# 이미지 경로
image_path = "/home/getout/workspace/watchbird/test_image/test3.png"

# inference 수행
result = CLIENT.infer(image_path, model_id="bird-v2-5op83/1")

# 결과 출력 (옵션)
print(json.dumps(result, indent=2))

# 이미지 로드
image = cv2.imread(image_path)

# 바운딩 박스 그리기
for prediction in result["predictions"]:
    x = int(prediction["x"])
    y = int(prediction["y"])
    w = int(prediction["width"])
    h = int(prediction["height"])
    class_name = prediction["class"]

    # 왼쪽 상단, 오른쪽 하단 좌표 계산
    x1 = int(x - w / 2)
    y1 = int(y - h / 2)
    x2 = int(x + w / 2)
    y2 = int(y + h / 2)

    # 사각형 그리기 및 클래스 이름 쓰기
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(image, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# 결과 이미지 저장
output_path = "/home/getout/workspace/watchbird/test_image/test3_result.png"
cv2.imwrite(output_path, image)
print(f"Result image saved to {output_path}")