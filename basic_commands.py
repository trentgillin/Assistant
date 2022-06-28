
import datetime
from speech import *
from Skills.secrets import wolfram_alpha
import wolframalpha
import re
import random
from Skills.responses import *


def tell_time():
    time = str(datetime.datetime.now())
    hour = time[11:13]
    min = time[14:16]
    hour_st = str(hour)
    if int(hour) > 12:
        hour_st = int(hour) - 12
        hour_st = str(hour_st)
        print(hour_st + ":" + min+" PM")
        speak("The time is" + hour_st + min + "PM")
    else:
        speak("The time is" + hour_st + min + "AM")
        print(hour_st + ":" + min + " AM")


def hello(q):
    if "hello" in q or "hi" in q:
        response = random.choice(greeting_responses)
        print(response)
        speak(response)
    else:
        print(q+", how may I be of service today")
        speak(str(q)+" how may i be of service today")


def tell_day(typed = False):
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1

    # this line tells us about the number
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        if typed == False:
            speak("The day is " + day_of_the_week)
        else:
            return "The day is "+ day_of_the_week


def tell_date():
    date = datetime.datetime.now()
    date = date.strftime("%B %d %Y")
    print("The date is "+ date)
    speak("The date is " + date)

def query_wolframalpha(q, typed = False):
    client = wolframalpha.Client(wolfram_alpha)
    if type == False: 
        print("I will look that up")
        speak("i will look that up")
        verb = q.split(' ', 3)[2]
        q = q.split(' ', 3)[3]
        res = client.query(q)
        answer = next(res.results).text
        answer = q + ' ' + verb + ' ' + answer
        print(answer)
        speak(answer)
    else:
        verb = q.split(' ', 3)[2]
        q = q.split(' ', 3)[3]
        res = client.query(q)
        answer = next(res.results).text
        answer = q + ' ' + verb + ' ' + answer
        return answer

def shut_down():
    print("Please verify shutdown by offering security clearance")
    speak("please verify shutdown by offering security clearance")
    clearance = listen()
    if clearance in pass_codes:
        print("Shutting down, talk to you later")
        speak("shutting down talk to you later")
        os.system("shutdown")
    else:
        print("That is incorrect, shutdown aborted")
        speak("That is incorrect, shutdown aborted")


