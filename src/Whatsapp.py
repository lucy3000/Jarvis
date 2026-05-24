import pywhatkit
import pyttsx3
import datetime
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime
from jarvis_voice import speak

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0,4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))

def sendMessage():
    speak("who do you wnat to message?")
    a = int(input('''Person 1 - 1
              Person 2 - 2'''))
    if a == 1:
        speak("What is the message")
        message = str(input("Enter the message- "))
        pywhatkit.sendwhatmsg("+49 17092042442", message,time_hour=strTime, time_min = update)
    elif a == 2:
        pass