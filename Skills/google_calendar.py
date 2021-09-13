from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
import pandas as pd
from speech import *
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def get_events():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    later = datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    later = later.isoformat() + 'Z'
    events_result = service.events().list(calendarId='primary', timeMin=now, timeMax=later,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    event_output = []
    if not events:
        print("You have no upcoming events")
        speak("you have no upcoming events")

    else:
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            end = event['end'].get('dateTime', event['end'].get('date'))
            result = [event['summary'],
                      start,
                      end,
                      event['id']]
            event_output.append(result)

        event_output = pd.DataFrame.from_records(event_output)
        event_output.columns = ['Event', 'Start', 'End', 'ID']
        # get number of events
        events_length = len(event_output.index)
        # get time of first event
        event_time = event_output.Start[0][11:13]
        event_time = int(event_time)
        event_time = event_time - 12
        if events_length < 2:
            print("You have " + str(events_length) +" event in the next 24 hours")
            speak("You have " + str(events_length) + " event in the next 24 hours")
        else:
            print("You have " + str(events_length) + " events in the next 24 hours")
            speak("You have " + str(events_length) + " events in the next 24 hours")
        print("Your next event is "+str(event_output.Event[0])+" at "+str(event_time)+" o'clock")
        speak("Your next event is " + str(event_output.Event[0]) + " at " + str(event_time) + "o clock")

