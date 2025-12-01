count = 0
while count < 50:
  if mcp.read_adc(MIC) > sound_threshold:
	GPIO.output(LED, GPIO.HIGH)
  time.sleep(0.1)
  count += 1
  GPIO.output(LED,GPIO.LOW)
