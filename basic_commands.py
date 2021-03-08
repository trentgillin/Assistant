
import datetime
from speech import *


def tell_time():
    time = str(datetime.datetime.now())
    hour = time[11:13]
    min = time[14:16]
    hour_st = int(hour) - 12
    hour_st = str(hour_st)
    if int(hour) > 12:
        print(hour_st + ":" + min+" PM")
        speak("The time is" + hour_st + min + "PM")
    else:
        speak("Time time is" + hour_st + min + "AM")
        print(hour_st + ":" + min + " AM")


def hello(q):
    if "hello" in q:
        print("Hello, I am linus your personal assistant. Tell me how may I help you")
        speak("hello I am linus your personal assistant. Tell me how may I help you")
    else:
        print(q+", how may I be of service today")
        speak(str(q)+" how may i be of service today")


def tell_day():
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
        speak("The day is " + day_of_the_week)


def tell_date():
    date = datetime.datetime.now()
    date = date.strftime("%B %d %Y")
    speak("The date is " + date)

