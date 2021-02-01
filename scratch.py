from vosk import Model, KaldiRecognizer
import pyaudio
import time
import json

def listen():
     p = pyaudio.PyAudio()
     stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
     stream.start_stream()

     model = Model("model")
     rec = KaldiRecognizer(model, 16000)

     print("listening. . .")

     time_duration = 3
     time_start = time.time()

     query = []
     while time.time() < time_start + time_duration:
         data = stream.read(2000, exception_on_overflow=False)
         rec.AcceptWaveform(data)
         #rec.Result()
         result = rec.PartialResult()
         words = json.loads(result)['partial']
         query.append(words)

     # remove spaces
     #query = ' '.join(query).split()

     # join strings together to make one statement
     #query = ' '.join(query)
     query = query[-1]
     return query



