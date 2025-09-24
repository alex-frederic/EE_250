# Name: Alex Frederic
# GitHub: https://github.com/alex-frederic/EE_250.git
# GitHub Username: alex-frederic

import paho.mqtt.client as mqtt
import time

# Callback function for connecting to the RPi broker
def on_connect(client, userdata, flags, rc):
	# Confirm connection to the broker in the console
	print("Connected to RPi broker with result code " + str(rc))

	# Subscribe to ping topic
	client.subscribe("arfreder/ping")

	# Create custom callback
	client.message_callback_add("arfreder/ping", on_ping)

# Custom callback function for receiving a pong message from the other client
def on_ping(client, userdata, message):
	# Convert received message from ping topic to int and print to console
	received = int( message.payload.decode() )
	print("Ping: " + str(received))
	
	# Wait a second and then publish the 1 + the received message to the pong topic
	time.sleep(1)
	client.publish( "arfreder/pong",  str( received + 1 ) )

if __name__ == '__main__':
	# Create a client object
	client = mqtt.Client()

	# Define on_connect callback function
	client.on_connect = on_connect

	# Connect to RPi broker
	client.connect(host="test.mosquitto.org", port=1883, keepalive=60)

	# Loop forever while managing connections
	client.loop_forever()