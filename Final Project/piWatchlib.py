def display_alert(image_path):
    import requests
    import os

    # 1. Configuration
    # The URL from your screenshot (Test URL)
    N8N_WEBHOOK_URL = 'http://localhost:5678/webhook/send-sms-alert'

    # Check if file exists first
    if not os.path.exists(image_path):
        print(f"❌ Error: File not found at {image_path}")
        print("Please edit the IMAGE_PATH variable in the script.")
        return

    print(f"Attempting to upload: {image_path}")
    
    # Open the file in binary mode
    with open(image_path, 'rb') as img_file:
        # 2. Prepare the payload
        # 'file' is the key name n8n will see in the Binary tab
        files = {
            'file': (image_path, img_file, 'image/jpeg')
        }

        try:
            # 3. Send the POST request
            response = requests.post(N8N_WEBHOOK_URL, files=files)
            
            # 4. Check results
            if response.status_code == 200:
                print("✅ Success! Image sent to n8n.")
                print("Check your n8n Webhook node output under the 'Binary' tab.")
            else:
                print(f"⚠️ Failed with Status Code: {response.status_code}")
                print(f"Response: {response.text}")

        except requests.exceptions.ConnectionError:
            print(f"❌ Connection Refused. Is n8n running and listening on localhost:5678?")

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