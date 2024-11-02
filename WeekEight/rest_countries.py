"""
Country Information Retriever
Author: Sohaib Mohiuddin
Date: 11/01/2024

Description:
This script fetches and displays information about a country using the REST Countries API. 
It retrieves data like the capital, population, area, languages, region, and subregion.
"""

import requests

# This function will communicate with RESTCountries API to pull data about a specific country
def retrieve_country_data(country):
    api_endpoint = f'https://restcountries.com/v3.1/name/{ country }'
    
    try:
        response = requests.get(api_endpoint)
        response.raise_for_status()
        
        # retrieve the first match from the search
        data = response.json()[0]
        
        return data
    
    except requests.exceptions.HTTPError:
        print(f'Error: Country not found! Please check spelling and try again!')
        return None
    except requests.exceptions.RequestException as re:
        print(f'Error: Unable to communicate with API - { re }')
        return None
    
# This function will display the pulled country data in a parsed manner
def display_country_data(data):
    # Get All Data 
    country_name = data['name']['common']
    capital_name = data.get('capital', ['Unable To Retrieve Capital'])[0]
    population = data.get('population', 'Unable To Retrieve Population')
    area = data.get('area', 'Unable To Retrieve Area')
    languages = ', '.join(data['languages'].values()) if 'languages' in data else 'Unable To Retrieve Languages'
    
    print('\nCountry Information')
    print('*' * 20)
    print(f'Country Name - { country_name }')
    print(f'Capital City - { capital_name }')
    print(f'Population - { population }')
    print(f'Area - { area } Square Kilometers')
    print(f'Languages - { languages }')
    

if __name__ == "__main__":
    # country = input("Enter the name of a country: ").strip()
    country_data = retrieve_country_data('Canada')
    
    display_country_data(country_data)