#!/usr/bin/python3
# Main script for assistant, sets up engine and determines what commands to execute based off of input

# modules
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
            tell_day()
            break

        elif "what time is it" in query:
            tell_time()
            break

        elif "what is the date" in query:
            tell_date()
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
            print("Goodbye, speak with you soon!")
            speak("Goodbye, speak with you soon")
            break

        elif query in greetings:
            hello(query)
            break

        elif query in event_queries:
            get_events()
            break

        elif "what is your name" in query:
            print("I am linus, your personal assistant")
            speak("I am linus your personal assistant")
            break

        elif "what is your favorite color" in query:
            print("I like them all but I am partial to monochromatic wavelengths")
            speak("I like them all but I am partial to monochromatic wavelengths")
            break

        elif query in ["create event", "add event"]:
            #create_event()
            print("This is still a work in progress, check back later")
            speak("This is still a work in progress, check back later")
            break

        elif "look up" in query:
            query_wolframalpha(query)
            break

        elif query in ["shutdown", "turn off computer"]:
            shut_down()
            break

        # catch all if does not know command
        else:
            print("Im not sure how to do that")
            speak("im not sure how to do that")
            break


if __name__ == '__main__':
    model_loaded = os.path.abspath('model')
    while True:
        q = listen(model_loaded).lower()
        if "linus" in q:
            print("You said: "+q)
            take_query(q)
            continue

        elif "stop listening" in q:
            exit()

        else:
            print("Awaiting commands")
            time.sleep(2)
            continue





