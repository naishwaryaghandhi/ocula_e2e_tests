import requests
import pytest
import configparser

# Read API key from config file
config = configparser.ConfigParser()
config.read('resources/config.ini')
API_KEY = config['openweathermap']['api_key']

URL = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=" + API_KEY
response = requests.get(URL)
json_data = response.json()


def test_weather_api_status_code():
    assert response.status_code == 200


def test_weather_temperature():
    if response.status_code == 200:
        assert "temp" in json_data["main"]


def test_weather_temperature_min():
    if response.status_code == 200:
        assert "temp_min" in json_data["main"]


def test_weather_temperature_max():
    if response.status_code == 200:
        assert "temp_max" in json_data["main"]


def test_weather_humidity():
    if response.status_code == 200:
        assert "humidity" in json_data["main"]


if __name__ == '__main__':
    pytest.main()
