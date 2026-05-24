#import libaries
import pyttsx3 #text-to-speech libary
import datetime
from jarvis_voice import speak

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour <= 12:
        speak ("Good Morning, sir")
    elif hour >12 and hour <= 18:
        speak("Good Afternoon, sir")
    else:
        speak("Good Evening, sir")
    
    speak("How can I help you?")