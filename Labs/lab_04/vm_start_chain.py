# Name: Alex Frederic
# GitHub: https://github.com/alex-frederic/EE_250.git
# GitHub Username: alex-frederic

import paho.mqtt.client as mqtt
import time

# Callback function for connecting to the RPi broker
def on_connect(client, userdata, flags, rc):
	print("Connected to RPi broker with result code " + str(rc))

	# Subscribe to pong topic
	client.subscribe("arfreder/pong")

	# Create custom callback
	client.message_callback_add("arfreder/pong", on_pong)

def on_pong(client, userdata, message):
	# Convert received message from pong topic to int and print to console
	received = int( message.payload.decode() )
	print("Pong: " + str(received))
	
	# Wait a second and then publish the 1 + the received message to the ping topic
	time.sleep(1)
	client.publish( "arfreder/ping", str( received + 1 ) )
    
if __name__ == '__main__':
	# Create a client object
	client = mqtt.Client()

	# Define on_connect callback function
	client.on_connect = on_connect

	# Connect to RPi broker
	client.connect(host="test.mosquitto.org", port=1883, keepalive=60)

	# Publish initial "1" message to the ping topic to start the chain
	client.publish("arfreder/ping", "1")

	# Loop forever while managing connections
	client.loop_forever()