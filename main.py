# Main script for assistant, sets up engine and determines what commands to execute based off of input

# modules
from basic_commands import *
from Skills.weather import *
from vosk import Model
from Skills.query_types import *

def take_query(model_loaded, q):

    # the program
    while True:
        time.sleep(2)
        # taking the query and making it into
        # lower case so that most of the times
        # query matches and we get the perfect
        # output
        #query = listen(model_loaded).lower()
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

        elif "what's the weather" in query:
            # get city from request
            user_city = query.split()
            user_city = user_city[-2:]
            user_city = " ".join(user_city)

            print("Getting weather for "+user_city+" . . .")
            speak("getting weather for "+user_city)

            # build report
            r = WeatherReport(user_city)
            r.lat_long = r.geocode()
            r.weather_results = r.get_weather()
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

        # catch all if does not know command
        else:
            print("Im not sure how to do that")
            speak("im not sure how to do that")
            break


if __name__ == '__main__':

    while True:
        model_loaded = Model("model")
        first_command = listen(model_loaded).lower()
        first_command = first_command.split()
        if not first_command:
            print("Awaiting commands")
            continue
        else:
            address = first_command.pop(0)
        if "linus" in address:
            q = " ".join(first_command)
            print("You said: "+q)
            take_query(model_loaded, q)
            continue

        elif "stop listening" in first_command:
            exit()

        else:
            print("Awaiting commands")
            time.sleep(2)
            continue







