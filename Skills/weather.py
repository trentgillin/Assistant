# code to get weather for user-defined city

# modules
import requests
import json
from Skills.secrets import api_key

# class for weather forecast
class WeatherReport:
    def __init__(self, city):
        self.city = city

    # method to get lat on logitude of city
    def geocode(self):
        url = "http://api.openweathermap.org/geo/1.0/direct?q="+self.city+"&limit=5&appid="+api_key
        result_geo = requests.get(url)
        lat_lon = json.dumps(result_geo.json(), sort_keys=True, indent=4)
        print(lat_lon)



