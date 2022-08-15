import speech_recognition as sr
import os

def listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source , duration= 0.2)
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source,phrase_time_limit=2)

    try:
        print("Recognizing..")
        command = r.recognize_google(audio , language="en-in")
        print(f"you said : {command}")

    except:
        return ""

    command = str(command)
    return command.lower()


while True:

    wake_up = listen()

    if 'wake up' in wake_up or 'sunday' in wake_up:
        os.startfile('d:\\nikhil python\\sunday ai\\sunday.py')   
        break