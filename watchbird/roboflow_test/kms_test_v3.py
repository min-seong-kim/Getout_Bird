import supervision as sv
from PIL import Image

# Load the image
image = Image.open("/home/getout/workspace/watchbird/test_image/test3.png")

# Get results
results = CLIENT.infer(
    "/home/getout/workspace/watchbird/test_image/test3.png", 
    model_id="bird-v2-5op83/1"
)

# Convert results to detections
detections = sv.Detections.from_inference(results[0])

# Create annotators
box_annotator = sv.BoxAnnotator()
label_annotator = sv.LabelAnnotator()

# Annotate image
annotated_image = box_annotator.annotate(scene=image, detections=detections)
annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections)

# Display the image
sv.plot_image(image=annotated_image, size=(16, 16))
