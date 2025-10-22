try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing")


import time

GPIO.setmode(GPIO.BOARD)

# LED Output
LED = [11]
GPIO.setup(LED, GPIO.OUT)


while True:
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.5)

GPIO.cleanup()
