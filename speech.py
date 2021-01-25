import pyttsx3
import speech_recognition as sr

def speak(audio):
    engine = pyttsx3.init()
    # slow the rate
    #engine.setProperty('rate', 180)
    # getter method(gets the current value
    # of engine property)
    voices = engine.getProperty('voices')

    # setter method .[0]=male voice and
    # [1]=female voice in set Property.
    engine.setProperty('voice', voices[12].id)

   # set rate of voices
   engine.setProperty('rate', 145)

   # Method for the speaking of the the assistant
    engine.say(audio)

    # Blocks while processing all the currently
    # queued commands
    engine.runAndWait()

# this method is for taking the commands
# and recognizing the command from the
# speech_Recognition module we will use
# the recongizer method for recognizing
def takeCommand():
    r = sr.Recognizer()

    # from the speech_Recognition module
    # we will use the Microphone module
    # for listening the command
    with sr.Microphone() as source:
        print('Listening. . .')

        # seconds of non-speaking audio before
        # a phrase is considered complete
        r.pause_threshold = 0.8
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

        # Now we will be using the try and catch
        # method so that if sound is recognized
        # it is good else we will have exception
        # handling
        try:
            print("Recognizing. . .")

            # for Listening the command in indian
            # english we can also use 'hi-In'
            # for hindi recognizing
            Query = r.recognize_google(audio, language='en-in')
            print("You said: ", Query)

        except Exception as e:
            print(e)
            print("i am sorry I did not understand")
            return "None"

        return Query

def takefirst():
    r = sr.Recognizer()

    # from the speech_Recognition module
    # we will use the Microphone module
    # for listening the command
    with sr.Microphone() as source:
        print('Listening. . .')

        # seconds of non-speaking audio before
        # a phrase is considered complete
        r.pause_threshold = 0.8
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

        # Now we will be using the try and catch
        # method so that if sound is recognized
        # it is good else we will have exception
        # handling
        try:
            first_command = r.recognize_google(audio, language='en-in')
            print("You said: ", first_command)

        except Exception as e:
            print(e)
            print("I am sorry I did not understand")
            return "None"

        return first_command
