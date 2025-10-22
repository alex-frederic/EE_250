import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

#using physical pin 11 to blink an LED
GPIO.setmode(GPIO.BOARD)
chan_list = [11]
GPIO.setup(chan_list, GPIO.OUT)

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# by taking readings and printing them out, find
# appropriate threshold levels and set them 
# accordingly. Then, use them to determine
# when it is light or dark, quiet or loud.
lux_threshold=40  # change this value
sound_threshold=700 # change this value

LED = 11
LIGHT_SENSOR = 0
MIC = 1

while True: 
  #Following commands control the state of the output
  #GPIO.output(pin, GPIO.HIGH)
  #GPIO.output(pin, GPIO.LOW)
  for i in range(5):
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.5)
  
  count = 0
  while count < 50:
    lux_val = mcp.read_adc(LIGHT_SENSOR)
    if lux_val > lux_threshold:
      print(f"{lux_val}: Bright")
    else:
      print(f"{lux_val}: Dark")

    count += 1
    time.sleep(0.1)
  
  for i in range(4):
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.2)
  
  count = 0
  while count < 50:
    mic = mcp.read_adc(MIC)
    print(f"MIC: {mic}")
    if mic > sound_threshold:
      GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.1)
    
    count += 1
    GPIO.output(LED, GPIO.LOW)
