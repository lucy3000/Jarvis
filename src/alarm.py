import pyttsx3
import datetime
import os
from jarvis_voice import speak

with open("Alarm.txt", "rt") as extractedtime:
    time = extractedtime.read()

with open("Alarm.txt", "r+") as deletetime:
    deletetime.truncate(0)

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("jarvis", "").replace("set an alarm", "").replace("and", ":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak("Alarm ringing, sir")
            os.startfile("music.mp3")
            break
        elif datetime.datetime.strptime(currenttime, "%H:%M:%S") + datetime.timedelta(seconds=30) == datetime.datetime.strptime(Alarmtime, "%H:%M:%S"):
            exit()

ring(time)
