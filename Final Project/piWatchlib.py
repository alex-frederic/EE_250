import requests
def display_alert():
    print("Displaying alert")
    requests.post('http://localhost:5678/webhook/send-sms-alert')
def display_image(image_path):
    print(f"Replacing previous image with new image @{image_path}")
def log_image(image_path):
    print(f"Logging image @{image_path}")
def current_time():
    import time
    return time.strftime("%Y%m%d-%H%M%S")

def send_image(image_path='image.jpg', HOST='172.20.10.5', PORT=65432):
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        # Read the image file in binary mode
        with open(image_path, 'rb') as f:
            image_data = f.read()
        
        s.sendall(image_data)
        print("Image sent successfully.")