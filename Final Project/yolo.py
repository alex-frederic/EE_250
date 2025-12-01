from ultralytics import YOLO
import cv2

def runInference(img):
    # Load model (choose yolov8n.pt for smallest model)
    model = YOLO("yolov8n.pt")

    # Load Image and Run inference
    results = model(cv2.imread(img))

    # Show result
    annotated = results[0].plot()
    f = open("inference_output.jpg", "wb")
    f.write(annotated)
    f.close()