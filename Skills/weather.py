# code to get weather for user-defined city

# modules
import requests
import json
from Skills.secrets import weather_api_key
import geocoder
from speech import *

# class for weather forecast
class WeatherReport:
    def __init__(self, city):
        self.city = city

    # method to get lat on logitude of city
    def geocode(self):
        g = geocoder.osm(self.city)
        lat_long = g.latlng
        return(lat_long)

    # function to get current weather
    def get_weather(self):
        url = "https://api.openweathermap.org/data/2.5/onecall?lat="+str(self.lat_long[0])+"&lon="+str(self.lat_long[1])+"&exclude=hourly&appid="+weather_api_key+"&units=imperial"
        result = requests.get(url)
        weather = json.loads(result.text)
        current_weather = weather['current']
        current_temp = current_weather['temp']
        current_feelslike = current_weather['feels_like']
        sky_conditions = current_weather['weather'][0]['description']

        weather_report = {
            "temp": current_temp,
            "feels_like": current_feelslike,
            "sky": sky_conditions
        }

        return weather_report

    def speak_weather(self):
        # speak report
        print("currently in " + self.city + " the weather is " + str(self.weather_results['temp']) + " degrees farenheit "
                                                                                                  "and feels like " + str(
            self.weather_results['feels_like']) + " with " + str(self.weather_results['sky']))

        speak("currently in " + self.city + " the weather is " + str(self.weather_results['temp']) + " degrees farenheit "
                                                                                                  "and feels like " + str(
            self.weather_results['feels_like']) + " with " + str(self.weather_results['sky']))



