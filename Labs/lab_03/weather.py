import requests
import json

# WeatherAPI key
WEATHER_API_KEY = '3f5479e70c3f40b29e121019252009'  # TODO: Replace with your own WeatherAPI key

def get_weather(city):
    # TODO: Build the API request URL using the base API endpoint, the API key, and the city name provided by the user.
    URL = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}"

    # TODO: Make the HTTP request to fetch weather data using the 'requests' library.
    response = requests.get(URL)
    
    # TODO: Handle HTTP status codes:
    # - Check if the status code is 200 (OK), meaning the request was successful.
    # - If not 200, handle common errors like 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), and any other relevant codes.
    
    if response.status_code == 200:
        # TODO: Parse the JSON data returned by the API. Extract and process the following information:
        # - Current temperature in Fahrenheit
        # - The "feels like" temperature
        # - Weather condition (e.g., sunny, cloudy, rainy)
        # - Humidity percentage
        # - Wind speed and direction
        # - Atmospheric pressure in mb
        # - UV Index value
        # - Cloud cover percentage
        # - Visibility in miles

        data = response.json()
        curr_data = data["current"]

        relevant_data = {
                "Temp: %s°F" : curr_data["temp_f"],
                "Feels Like: %s°F" : curr_data["feelslike_f"],
                "Condition: %s" : curr_data["condition"]["text"],
                "Humidity: %s%%" : curr_data["humidity"],
                "Wind Speed: %s mi/h" : curr_data["wind_mph"],
                "Wind Direction: %s" : curr_data["wind_dir"],
                "Pressure: %s mb" : curr_data["pressure_mb"],
                "UV Index: %s" : curr_data["uv"],
                "Cloud Cover: %s" : curr_data["cloud"],
                "Visibility: %s mi" : curr_data["vis_miles"]
        }

        # TODO: Display the extracted weather information in a well-formatted manner.
        print(f"Weather data for {city}...")

        print()
        for (format_str, value) in relevant_data.items():
            print(format_str %value)
        
    else:
        # TODO: Implement error handling for common status codes. Provide meaningful error messages based on the status code.
        print(f"Error: {response.status_code}. Something went wrong.")

        if response.status_code == 400:
            print("Bad Request: Could not process your request. Please rephrase it.")
        elif response.status_code == 401:
            print("Unauthorized: Your request lacked valid authentification to access the requested resource.")
        elif response.status_code == 403:
            print("Forbidden: You do not have valid access to the requested materials based on your provided authentification.")
        elif response.status_code == 404:
            print("Not Found: The server could not find the resource you requested. It may not exisst.")


if __name__ == '__main__':
    # TODO: Prompt the user to input a city name.
    city = input("Enter city: ")

    # TODO: Call the 'get_weather' function with the city name provided by the user.
    get_weather(city)
