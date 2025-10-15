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

# max_ult = 0
while True:
  try:
    # TODO:read distance value from Ultrasonic Ranger and print distance on LCD
    ult = grovepi.ultrasonicRead(ultrasonic_ranger)
    # if ult > max_ult and ult < 60000:
    #   max_ult = ult
    # print(str(ult) + ", " + str(max_ult))

    # TODO: read threshold from potentiometer
    pot = grovepi.analogRead(potentiometer)
    
    MAX_ULT = 507
    MAX_POT = 1023
    threshold = pot * (MAX_ULT / MAX_POT)
    
    too_close = ult < threshold

    # TODO: format LCD text according to threshhold
    obj_alert = "OBJ_PRES" if too_close else "        "
    disp = "%3dcm %s\n%3dcm" %(threshold, obj_alert, ult)

    setText_norefresh(disp)

    if too_close:
      setRGB(255,0,0)
    else:
      setRGB(0,255,0)

  except IOError:
    print("Error")
