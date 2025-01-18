#!/usr/bin/env python3


'''
Day 13: Using External Libraries: Requests
- Topics:
 - Learn how to make HTTP requests with the requests library.
 - Understanding HTTP methods: GET, POST.

- Project:
 - Create a Python script that fetches data from a public API (e.g., OpenWeatherMap) and displays the
weather.


How It Works

 This script fetches the current weather for a given city using the WTTR.in API.
 It prompts the user for a city name, sends an HTTP GET request, and parses the JSON response.
 The script displays the weather description and temperature in Celsius or an error message if the request fails.


'''

print("\nA SIMPLE PYTHON PROGRAM TO FETCH WEATHER DATA FOR A CITY USING WTTR.in API\n")


import requests

# Base URL for WTTR.in
BASE_URL = "https://wttr.in"

# Function to fetch weather data
def get_weather(city):
    # Append the city name and specify the response format as JSON
    url = f"{BASE_URL}/{city}?format=j1"

    # Make a GET request
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Extract current weather information
        current = data["current_condition"][0]
        weather = current["weatherDesc"][0]["value"]
        temp = current["temp_C"]
        print(f"The weather in {city} is {weather} with a temperature of {temp}°C.")
    else:
        print("Error fetching weather data.")

# Ask the user for a city
city_name = input("Enter the name of the city: ")
get_weather(city_name)
