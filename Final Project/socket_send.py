import socket
from yolo import runInference
import cv2

HOST = '172.20.10.3'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    # Read the image file in binary mode
    # with open('image.jpg', 'rb') as f:
    #     image_data = f.read()
    annotated = runInference('image.jpg')
    # Send the image data
    success, encoded = cv2.imencode(".jpg", annotated)
    img_bytes = encoded.tobytes()
    s.sendall(img_bytes)
    print("Image sent successfully.")
