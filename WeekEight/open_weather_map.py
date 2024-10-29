"""
OpenWeatherMap API Demonstration
Author: Sohaib Mohiuddin

Description:
This program communicates with the OpenWeatherMap API to retrieve the current 
weather for a specified city. It displays temperature, weather description, 
and humidity.
"""

import requests
from 

# Constants
API_KEY = "your_api_key_here"  # Replace with your actual API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city_name):
    """Fetch weather data from OpenWeatherMap for a given city."""
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  # Use 'metric' for Celsius
    }
    
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()  # Convert JSON response to a dictionary
        return data
    else:
        print(f"Error: {response.status_code} - {response.reason}")
        return None

def display_weather(data):
    """Display key weather information from the API response."""
    city = data['name']
    country = data['sys']['country']
    temperature = data['main']['temp']
    weather_description = data['weather'][0]['description']
    humidity = data['main']['humidity']

    print(f"\nWeather in {city}, {country}:")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {weather_description.capitalize()}")
    print(f"Humidity: {humidity}%")

if __name__ == "__main__":
    city_name = input("Enter the name of the city: ").strip()
    weather_data = get_weather_data(city_name)

    if weather_data:
        display_weather(weather_data)
