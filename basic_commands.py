
import datetime
from speech import *


def tell_time():
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is" + hour + "Hours and" + min + "Minutes")


def hello(q):
    if "hello" in q:
        print("Hello sir, I am linus. Tell me how may I help you")
        speak("hello sir I am linus. Tell me how may I help you")
    else:
        print(q+" sir, how may I be of service today")
        speak(str(q)+" sir how may i be of service today")


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

