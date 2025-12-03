import socket

HOST = '172.20.10.3'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    # Read the image file in binary mode
    with open('test.jpg', 'rb') as f:
        image_data = f.read()
    
    # Send the image data
    s.sendall(image_data)
    print("Image sent successfully.")
