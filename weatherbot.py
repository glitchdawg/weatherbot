import requests
from pprint import pprint
import config

city=input("Enter a city: ")
base_url='http://api.openweathermap.org/data/2.5/weather?appid='+config.API_KEY+'&q='+city

weather_data = requests.get(base_url).json()

pprint(weather_data)



