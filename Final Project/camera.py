import picamera
from time import sleep
# from yolo import runInference

camera = picamera.PiCamera()


camera.start_preview()

sleep(5)
camera.capture('./scan.jpg')

# with open("./scan.jpg") as file:


camera.stop_preview()