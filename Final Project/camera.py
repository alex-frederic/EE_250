import picamera
from time import sleep

def take_pic():
	camera = picamera.PiCamera()
	camera.start_preview()

	print("Taking image...")
	camera.capture('./piwatch_photo.jpg')

	camera.stop_preview()