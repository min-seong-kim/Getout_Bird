from inference_sdk import InferenceHTTPClient

client = InferenceHTTPClient(
    api_url="http://localhost:9001"  # 로컬 inference 서버 사용
)

image_path = "/home/getout/workspace/watchbird/test_image/test3.png"

result = client.infer(
    image_path,
    model_id="bird-v2-5op83/1"  # 당신이 만든 모델 ID
)

print(result)
