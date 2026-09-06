import requests
import json
from datetime import datetime
import sys

GEOCODING_URL = 'https://geocoding-api.open-meteo.com/v1/search'
WEATHER_URL = 'https://api.open-meteo.com/v1/forecast'

def get_coordinates(city):
    try:
        params = {
            'name': city,
            'count': 1,
            'format': 'json'
        }
        response = requests.get(GEOCODING_URL, params=params)
        response.raise_for_status()
        data = response.json()
        if data.get('results'):
            return data['results'][0]['latitude'], data['results'][0]['longitude']
        else:
            print(f"City '{city}' not found. API response: {data}")
            return None, None
    except Exception as e:
        print(f"Error fetching coordinates: {e}")
        return None, None

def get_weather(latitude, longitude):
    try:
        params = {
            'latitude': latitude,
            'longitude': longitude,
            'current_weather': True
        }
        response = requests.get(WEATHER_URL, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching weather: {e}")
        return None

def save_to_file(city, data, filename='weather_data.txt'):
    try:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(filename, 'a') as f:
            f.write(f"Time: {timestamp}\n")
            f.write(f"City: {city}\n")
            f.write(f"Temperature: {data['current_weather']['temperature']}°C\n")
            f.write(f"Weather Code: {data['current_weather']['weathercode']}\n")
            f.write("\n")
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 weather_fetcher.py <city_name1> <city_name2> ...")
        return
    
    for city in sys.argv[1:]:
        print(f"\nFetching weather for {city}...")
        latitude, longitude = get_coordinates(city)
        if latitude and longitude:
            weather_data = get_weather(latitude, longitude)
            if weather_data:
                save_to_file(city, weather_data)

if __name__ == "__main__":
    main()