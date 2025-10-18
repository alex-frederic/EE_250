# Team Members: Alex Frederic (GitHub: alex-frederic, arfreder@usc.edu)
#               Peyton Crawford

# NOTE: Always run with the "python3" command, not just "python"

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

# clear lcd screen before starting main loop
setText("")

# Only uncomment if testing max Ultrasonic Ranger output
# max_distance = 0

while True:
  try:
    # TODO:read distance value from Ultrasonic Ranger and print distance on LCD
    distance = grovepi.ultrasonicRead(ultrasonic_ranger)

    # Code for detecting the maximum output of the Ultrasonic Ranger
    # if distance > max_distance and distance < 60000:
    #   max_distance = distance
    # print(str(distance) + ", " + str(max_distance))

    # TODO: read threshold from potentiometer
    pot = grovepi.analogRead(potentiometer)
    
    MAX_DIST = 507
    MAX_POT = 1023
    threshold = int( pot * (MAX_DIST / MAX_POT) )

    too_close = distance < threshold

    # TODO: format LCD text according to threshhold

    obj_alert = "OBJ_PRES" if too_close else "          "
    # NOTE: The field of spaces is intentionally 2 characters longer than "OBJ_PRES".
    # This helps with a bug wherein the letter "ES" appear to the left of where the text
    # is meant to appear when the text changes really quickly. These extraneous characters
    # don't get erased along with the rest of the text unless the space field is 2
    # characters longer than the alert text, so this prevents them from lingering there
    # for the rest of the program's runtime.

    disp = "%3dcm %s\n%3dcm" %(threshold, obj_alert, distance)

    setText_norefresh(disp)

    # Set color appropriately for given distance and threshold values
    if too_close:
      setRGB(255,0,0)
    else:
      setRGB(0,255,0)

  except IOError:
    print("Error")
