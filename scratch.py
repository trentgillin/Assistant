from Skills.secrets import *
import json
import requests
import pandas as pd


def get_weather():
        url = "https://api.openweathermap.org/data/2.5/onecall?lat=33.7489924&lon=-84.3902644&exclude=hourly&appid="+api_key+"&units=imperial"
        result = requests.get(url)
        weather = json.loads(result.text)
        current_weather = weather['current']
        current_temp = current_weather['temp']
        current_feelslike = current_weather['feels_like']
        sky_conditions = current_weather['weather'][0]['description']

        weather_report = {
                "temp": current_temp,
                "feelslike": current_feelslike,
                "sky": sky_conditions
        }

        return weather_report
