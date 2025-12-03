import socket
from yolo import runInference
import cv2

def receive_image(HOST='127.0.0.1', PORT=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            # Receive the image data
            image_data = b''
            while True:
                chunk = conn.recv(4096)  # Receive data in chunks
                if not chunk:
                    break
                image_data += chunk
            
            # Save the received image
            with open('received_image.jpg', 'wb') as f:
                f.write(image_data)
            annotated = runInference('received_image.jpg')
            # Send the image data
            success, encoded = cv2.imencode(".jpg", annotated)
            img_bytes = encoded.tobytes()
            with open('annotated_received_image.jpg', 'wb') as f:
                f.write(img_bytes)
            print("Image received and saved as 'received_image.jpg'")
