import sys
sys.path.append('~/Dexter/GrovePi/Software/Python')
import time
import grovepi
from grove_rgb_lcd import *

# Grove Ultrasonic Ranger connectd to digital port 2
ultrasonic_ranger = 2
# potentiometer connected to analog port A0 as input
potentiometer = 0
grovepi.pinMode(potentiometer,"INPUT")

# clear lcd screen  before starting main loop
setText("")

max_ult = 0
while True:
  try:
    # TODO:read distance value from Ultrasonic Ranger and print distance on LCD
    ult = grovepi.ultrasonicRead(ultrasonic_ranger)
    if ult > max_ult and ult < 60000:
      max_ult = ult
    print(ult + ", " + max_ult)

    # TODO: read threshold from potentiometer
    pot = grovepi.analogRead(potentiometer)

    # TODO: format LCD text according to threshhold


  except IOError:
    print("Error")
