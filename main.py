# Main script for assistant, sets up engine and determines what commands to execute based off of input

# modules
from basic_commands import *
from Skills.weather import *
from Skills.google_calendar import *
from vosk import Model
from Skills.query_types import *


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

        # catch all if does not know command
        else:
            print("Im not sure how to do that")
            speak("im not sure how to do that")
            break


if __name__ == '__main__':

    model_loaded = Model("/home/trent/Projects/Assistant/model")
    while True:
        first_command = listen(model_loaded).lower()
        #first_command = first_command.split()
        if not first_command:
            print("Awaiting commands")
            continue
        else:
            #address = first_command.pop(0)
            address = first_command
        if "linus" in address:
            print("Yes")
            speak("yes ")
            q = listen(model_loaded).lower()
            print("You said: "+q)
            take_query(q)
            continue

        elif "stop listening" in first_command:
            exit()

        else:
            print("Awaiting commands")
            time.sleep(2)
            continue







