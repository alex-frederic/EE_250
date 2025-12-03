import picamera
from time import sleep
import os

def take_pic():
	file_path = "./piwatch_photo.jpg"

	if os.path.isfile(file_path):
		os.remove(file_path)
		print("File deleted successfully.")

	print("Initializing camera...")
	camera = picamera.PiCamera()
	print("Setting resolution...")
	camera.resolution = (640, 480)
	print("Starting preview...")
	camera.start_preview()

	print("Taking image...")
	sleep(5)
	camera.capture('./piwatch_photo.jpg')

	camera.stop_preview()