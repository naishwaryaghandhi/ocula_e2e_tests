import requests
import pytest
import configparser

# Read API key from config file
config = configparser.ConfigParser()
config.read('resources/config.ini')
API_KEY = config['openweathermap']['api_key']
CITY = "London"

URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
response = requests.get(URL)
json_data = response.json()

def test_weather_api_status_code():
    assert response.status_code == 200


def test_weather_temperature():
    if response.status_code == 200:
        temp = json_data["main"]['temp']
        assert temp is not None, f"Missing temperature for {CITY}"
        print(f"Verified temperature: {temp} for the given city: {CITY}")


def test_weather_temperature_min():
    if response.status_code == 200:
        min_temp = json_data["main"]['temp_min']
        assert min_temp is not None, f"Missing minimum temperature for {CITY}"
        print(f"Verified minimum temperature: {min_temp} for the given city: {CITY}")


def test_weather_temperature_max():
    if response.status_code == 200:
        max_temp = json_data["main"]['temp_max']
        assert max_temp is not None, f"Missing maximum temperature for {CITY}"
        print(f"Verified maximum temperature: {max_temp} for the given city: {CITY}")


def test_weather_humidity():
    if response.status_code == 200:
        humidity = json_data["main"]['humidity']
        assert humidity is not None, f"Missing humidity for {CITY}"
        print(f"Verified humidity: {humidity} for the given city: {CITY}")


if __name__ == '__main__':
    pytest.main()
