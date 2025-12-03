from piWatchlib import take_picture, send_image
import time
import socket
from camera import take_pic

def main():
    take_pic()
    image_path = 'piwatch_photo.jpg'
    HOST = '127.0.0.1'
    PORT = 65432

    # Send image every second
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        # Read the image file in binary mode
        with open(image_path, 'rb') as f:
            image_data = f.read()
        
        s.sendall(image_data)
        print("Image sent successfully.")
        # send_image('image.jpg', '127.0.0.1', 65432)
        s.close()
        time.sleep(1) 
    

if __name__ == "__main__":
    main()
    