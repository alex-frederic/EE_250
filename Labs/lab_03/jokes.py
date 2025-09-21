import requests
import json

URL = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(URL)
rand_joke = response.json()

if response.status_code == 200:
	print(f"Type: {rand_joke["type"]}")
	print(f"ID: {rand_joke["id"]}")
	print("(Press enter to hear punchline)\n")

	print(rand_joke["setup"])
	input()
	print(rand_joke["punchline"])
else:
	if response.status_code == 400:
		print("Bad Request: Could not process your request. Please rephrase it.")
	elif response.status_code == 401:
		print("Unauthorized: Your request lacked valid authentification to access the requested resource.")
	elif response.status_code == 403:
		print("Forbidden: You do not have valid access to the requested materials based on your provided authentification.")
	elif response.status_code == 404:
		print("Not Found: The server could not find the resource you requested. It may not exisst.")