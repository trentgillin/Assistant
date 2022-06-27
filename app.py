# modules
from types import resolve_bases
from flask import Flask, render_template, request
from basic_commands import *
from Skills.weather import *
from Skills.google_calendar import *
from vosk import Model
from Skills.query_types import *
from Skills.reminder import *
import os
from speech import *

def take_query(q):

    # the program
    while True:
        query = q

        if "what day is it" in query:
            response = tell_day(typed = True)
            break

        elif "what time is it" in query:
            response = tell_time()
            break

        elif "What is the date" in query:
            response = tell_date()
            break

        elif "set reminder" in query:
            subj = query.split('reminder ').pop(1)
            new_one = Reminder(subj)
            new_one.set_time()
            new_one.save_reminder()
            break

        elif "weather" in query:
            # get city from request
            user_city = query.split()
            user_city = user_city[-2:]
            user_city = " ".join(user_city)

            print("Getting weather for "+user_city+" . . .")
            speak("getting weather for "+user_city)

            # build report
            r = WeatherReport(user_city)
            r.lat_long = r.geocode()
            try:
                r.weather_results = r.get_weather()
            except:
                print("I seem to be having trouble, try again later")
                speak("I seem to be having trouble try again later")
            # speak weather
            r.speak_weather()
            break

        # this will exit and terminate the program
        elif "goodbye" in query:
            response = "Goodbye, speak with you soon!"
            speak("Goodbye, speak with you soon")
            break

        elif query in greetings:
            response = hello(query)
            break

        elif query in event_queries:
            response = get_events()
            break

        elif "what is your name" in query:
            response = "I am linus, your personal assistant"
            break

        elif "what is your favorite color" in query:
            response = "I like them all but I am partial to monochromatic wavelengths"
            speak("I like them all but I am partial to monochromatic wavelengths")
            break

        elif query in ["create event", "add event"]:
            #create_event()
            response = "This is still a work in progress, check back later"
            speak("This is still a work in progress, check back later")
            break

        elif "look up" in query:
            response = query_wolframalpha(query)
            break

        elif query in ["shutdown", "turn off computer"]:
            shut_down()
            break

        # catch all if does not know command
        else:
            response = "Im not sure how to do that"
            speak("im not sure how to do that")
            break
        
    return response



model_loaded = os.path.abspath('model')
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/get")
def get_linus_response():
    userText = request.args.get('msg')
    return take_query(userText)

if __name__ == '__main__':
    app.run(host="0.0.0.0")


