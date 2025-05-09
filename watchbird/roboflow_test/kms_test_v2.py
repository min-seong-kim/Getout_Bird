from inference_sdk import InferenceHTTPClient

client = InferenceHTTPClient(
    api_url="http://localhost:9001", # use local inference server
    # api_key="7Qu9IPVAZ7FNTC49jwAT" # optional to access your private data and models
)

result = client.run_workflow(
    workspace_name="roboflow-docs",
    workflow_id="model-comparison",
    images={
        "image": "/home/getout/workspace/watchbird/test_image/test3.png"
    },
    parameters={
        "model1": "yolov8n-640",
        "model2": "yolov11n-640"
    }
)

print(result)