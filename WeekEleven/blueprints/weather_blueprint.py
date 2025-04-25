from flask import Blueprint, render_template, redirect, url_for, request
from dotenv import load_dotenv
import requests, os

weather_blueprint = Blueprint('weather_blueprint', __name__, template_folder='templates')

@weather_blueprint.route('/', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
        
        weather_data = get_weather_data(city_name)
        
        if 
        
        return render_template('weatherApi/index.html', data=data, title='OpenWeatherMap Api Demo')
    return render_template('weatherApi/index.html', title='OpenWeatherMap Api')


def get_weather_data(city_name):
    # Load environment variables from .env file
    load_dotenv()
    
    # Constants
    API_KEY = os.getenv('API_KEY')
    API_URL = os.getenv('API_URL')
    API_UNITS = os.getenv('API_UNITS')
    
    """Fetch weather data from OpenWeatherMap for a given city."""
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': API_UNITS
    }
    
    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        data = response.json()  # Convert JSON response to a dictionary
        return data
    else:
        print(f"Error: {response.status_code} - {response.reason}")
        return None

def weather_parser(data):
    # Parse the weather data and return the relevant information in JSON
    city = data['name']

    