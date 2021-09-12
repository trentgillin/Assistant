from vosk import Model, KaldiRecognizer
import pyaudio
import time
import json
import pyttsx3

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say(audio)
    engine.runAndWait()

def listen(model_loaded):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
    stream.start_stream()

    #model = Model("model")
    model = model_loaded
    rec = KaldiRecognizer(model, 16000)

    print("listening. . .")

    time_duration = 4
    time_start = time.time()

    query = []
    while time.time() < time_start + time_duration:
        data = stream.read(2000, exception_on_overflow=False)
        rec.AcceptWaveform(data)
        result = rec.PartialResult()
        words = json.loads(result)['partial']
        query.append(words)

    # remove spaces and get final result
    query = query[-1]
    stream.stop_stream()
    stream.close()
    p.terminate()
    return query


