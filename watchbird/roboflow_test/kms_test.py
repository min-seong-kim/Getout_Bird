import os
import time
from inference_sdk import InferenceHTTPClient
import cv2
import json

# 클라이언트 생성
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="7Qu9IPVAZ7FNTC49jwAT"
)

# 이미지 경로
watch_directory = "/home/getout/workspace/watchbird/save"
output_directory = "/home/getout/workspace/watchbird/save_result"
save_bird_class_directory = "/home/getout/workspace/watchbird/save_bird_class"  # 클래스 저장 경로
model_id = "bird-v2-5op83/1"

def get_latest_file(directory):
    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    if not files:
        return None, None
    latest_file = max(files, key=os.path.getmtime)
    return latest_file, os.path.getmtime(latest_file)

def process_image(image_path):
    try:
        # inference 수행
        result = CLIENT.infer(image_path, model_id=model_id)

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

            # 클래스 이름 저장
            filename = os.path.basename(image_path)
            name, ext = os.path.splitext(filename)
            class_file_path = os.path.join(save_bird_class_directory, f"{name}.txt")
            with open(class_file_path, "w") as f:
                f.write(class_name)
            print(f"Class name saved to {class_file_path}")

            # 왼쪽 상단, 오른쪽 하단 좌표 계산
            x1 = int(x - w / 2)
            y1 = int(y - h / 2)
            x2 = int(x + w / 2)
            y2 = int(y + h / 2)

            # 사각형 그리기 및 클래스 이름 쓰기
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # 결과 이미지 저장
        filename = os.path.basename(image_path)
        name, ext = os.path.splitext(filename)
        output_path = os.path.join(output_directory, f"frame_result_{name.split('_')[-1]}{ext}")
        cv2.imwrite(output_path, image)
        print(f"Result image saved to {output_path}")

    except Exception as e:
        print(f"Error processing {image_path}: {e}")

if __name__ == "__main__":
    # save_bird_class 디렉토리가 없으면 생성
    if not os.path.exists(save_bird_class_directory):
        os.makedirs(save_bird_class_directory)

    last_modified_time = None
    latest_file = None

    while True:
        new_latest_file, new_modified_time = get_latest_file(watch_directory)

        if new_latest_file:
            if new_latest_file != latest_file or new_modified_time != last_modified_time:
                print(f"New or updated file detected: {new_latest_file}")
                process_image(new_latest_file)
                latest_file = new_latest_file
                last_modified_time = new_modified_time
        else:
            print(f"No files found in {watch_directory}")

        time.sleep(1)