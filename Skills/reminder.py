# functions to set timer/reminders

# modules
from datetime import datetime, timedelta
import os
import pandas as pd
from speech import *
from vosk import Model

# text to number function
def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

class Reminder:
    def __init__(self, subject):
        self.subject = subject

    def set_time(self):
        print("When would you like the reminder?")
        speak("when would you like the reminder")
        model_loaded = os.path.abspath('model')
        remind_time = listen(model_loaded).lower()
        print("ok setting the reminder for " + remind_time+" from now")
        speak("ok setting the reminder for " + remind_time+" from now")
        number = remind_time.split().pop(0)
        number = text2int(number)
        amount = remind_time.split().pop()
        current_time = datetime.now()
        if amount == 'minutes':
            future_time = current_time + timedelta(minutes=number)
        elif amount == "seconds":
            future_time = current_time + timedelta(seconds=number)
        elif amount == "hours":
            future_time = current_time + timedelta(hours=number)
        else:
            print("That is an invalid amount of time")
            speak("that is an invalid amount of time")
        self.future_time = future_time

    def save_reminder(self):
        print("Saving Reminder")
        speak("saving reminder")
        if(os.path.exists("memory/reminders.csv") == False):
            reminders = pd.DataFrame(list())
            reminders['time']=None
            reminders['subject']=None
            reminders.to_csv('memory/reminders.csv')
        
        reminders = pd.read_csv("memory/reminders.csv")
        new_reminder = {self.future_time:self.subject}
        new_reminder = pd.DataFrame.from_dict(new_reminder, orient='index')
        new_reminder['time'] = new_reminder.index
        tog = [reminders, new_reminder]
        tog = pd.concat(tog)
        tog.to_csv('memory/reminders.csv')

    def check_reminder():
        reminders = pd.read_csv("memory/reminders.csv")





        

