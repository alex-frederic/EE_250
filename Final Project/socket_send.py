import socket
# from yolo import runInference

def send_image(image_path='image.jpg', HOST='172.20.10.5', PORT=65432):
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    # Read the image file in binary mode
    with open(image_path, 'rb') as f:
        image_data = f.read()
    
    s.sendall(image_data)
    print("Image sent successfully.")
