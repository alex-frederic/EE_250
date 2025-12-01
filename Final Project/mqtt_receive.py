import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
	print("Connected to test.mosquitto.org")
	print("Result Code: " + str(rc))

	client.subscribe("piwatch/send_img")
	client.message_callback_add("piwatch/send_img", on_receive_img)
	
def on_receive_img(client, userdata, img):
	print("Received Image!")

	f = open("output.jpg", "wb")
	f.write(img)
	f.close()

def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))

if __name__ == '__main__':
	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect(host="test.mosquitto.org", port=1883, keepalive=60)
	client.loop_forever()