from __future__ import print_function
import os.path
import pandas as pd
from speech import *
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def get_events(typed = False):
    creds = None
    if os.path.exists('Skills/token.json'):
        creds = Credentials.from_authorized_user_file('Skills/token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'Skills/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('Skills/token.json', 'w') as token:
            token.write(creds.to_json())
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
    if typed == False:
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
            if event_time > 12:
                event_time = event_time - 12
            if events_length < 2:
                print("You have " + str(events_length) +" event in the next 24 hours")
                speak("You have " + str(events_length) + " event in the next 24 hours")
            else:
                print("You have " + str(events_length) + " events in the next 24 hours")
                speak("You have " + str(events_length) + " events in the next 24 hours")
            print("Your next event is "+str(event_output.Event[0])+" at "+str(event_time)+" o'clock")
            speak("Your next event is " + str(event_output.Event[0]) + " at " + str(event_time) + "o clock")
    else:
        if not events:
            r = "No new upcoming events"
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
            if event_time > 12:
                event_time = event_time - 12
            if events_length < 2:
                r = ("You have " + str(events_length) +" event in the next 24 hours")
            else:
                r = ("You have " + str(events_length) + " events in the next 24 hours")
            r = ("Your next event is "+str(event_output.Event[0])+" at "+str(event_time)+" o'clock")
            return r

