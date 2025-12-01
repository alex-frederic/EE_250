import paho.mqtt.client as mqtt
import time
import socket
from yolo import runInference

def on_connect(client, userdata, flags, rc):
	print("Connected to test.mosqsuitto.org")
	print("Result Code: " + str(rc))

if __name__ == '__main__':
	# name = socket.gethostname()
	# ip_address = socket.gethostbyname(name)
	# print("Publisher IP Address: " + ip_address)

	#create a client object
	client = mqtt.Client()
	
	#attach the on_connect() callback function defined above to the mqtt client
	client.on_connect = on_connect

	client.connect(host="test.mosquitto.org", port=1883, keepalive=60)

	client.loop_start()
	time.sleep(1)

	while True:
		byteArr = 0
		# with open("./rpicamexample.jpg",'rb') as file:
		# 	print("Reading Image File")
		# 	filecontent = file.read()
		# 	byteArr = bytearray(filecontent)
	


		client.publish("piwatch/send_img", "Test")

		break