import picamera
from time import sleep

def take_pic():
	camera = picamera.PiCamera()
	camera.resolution = (640, 480)
	camera.start_preview()

	print("Taking image...")
	camera.capture('./piwatch_photo.jpg')

	camera.stop_preview()