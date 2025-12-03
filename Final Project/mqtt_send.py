import paho.mqtt.client as mqtt
import time
# from yolo import runInference

def on_connect(client, userdata, flags, rc):
	print("Connected to test.mosqsuitto.org")
	print("Result Code: " + str(rc))

if __name__ == '__main__':
	#create a client object
	client = mqtt.Client()
	
	#attach the on_connect() callback function defined above to the mqtt client
	client.on_connect = on_connect

	client.connect(host="test.mosquitto.org", port=1883, keepalive=60)

	client.loop_start()
	time.sleep(1)
	count = 0
	while True:
		byteArr = 0
		with open("./rpicamexample.jpg",'rb') as file:
			print("Reading Image File")
			filecontent = file.read()
			byteArr = bytearray(filecontent)

		print("Publishing...")
		client.publish("piwatch/send_img", byteArr)

		time.sleep(2)
		count += 1
		if(count == 5):
			break