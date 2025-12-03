import picamera
from time import sleep

camera = picamera.PiCamera()
camera.start_preview()
sleep(5)
camera.capture('./test_img.jpg')
camera.stop_preview()