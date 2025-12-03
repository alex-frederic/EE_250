import socket
from yolo import runInference

HOST = '172.20.10.3'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

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
        print("Image received and saved as 'received_image.jpg'")
