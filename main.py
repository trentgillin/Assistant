# Main script for assistant, sets up engine and determines what commands to execute based off of input

# modules
from basic_commands import *
from speech import *
import time


def take_query():

    hello()

    # the program
    while True:

        # taking the query and making it into
        # lower case so that most of the times
        # query matches and we get the perfect
        # output
        query = listen().lower()

        if "what day is it" in query:
            tell_day()
            continue

        elif "what time is it" in query:
            tell_time()
            continue

        elif "what is todays date" in query:
            tell_date()
            continue

        # this will exit and terminate the program
        elif "goodbye" in query:
            print("Goodbye, speak with you soon!")
            speak("Goodbye, speak with you soon")
            break

        # catch all if does not know command
        else:
            print("I am sorry I do not know how to do that, maybe I need an upgrade?")
            speak("I am sorry I do not know how to do that, maybe I need an upgrade")


if __name__ == '__main__':

    while True:

        first_command = listen().lower()
        if "linus" in first_command:
            take_query()
            continue

        elif "stop listening" in first_command:
            exit()

        else:
            print("Awaiting commands")
            time.sleep(2)
            continue







