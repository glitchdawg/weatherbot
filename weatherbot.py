import requests
from pprint import pprint

API_KEY = 'c11d57999051f03cba808719c9653aeb'

city=input("Enter a city: ")
base_url='http://api.openweathermap.org/data/2.5/weather?appid='+API_KEY+'&q='+city

weather_data = requests.get(base_url).json()

pprint(weather_data)



