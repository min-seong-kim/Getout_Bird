from roboflow import Roboflow

rf = Roboflow(api_key="7Qu9IPVAZ7FNTC49jwAT")
project = rf.workspace().project("bird-v2")
model = project.version(2).model

# infer on a local image
print(model.predict("/home/getout/workspace/watchbird/test_image/test5.png", confidence=40, overlap=30).json())

model.predict("/home/getout/workspace/watchbird/test_image/test5.png", confidence=40, overlap=30).save("/home/getout/workspace/watchbird/save/test5_save.png")
