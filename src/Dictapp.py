import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep
from jarvis_voice import speak

dictapp = {"commandprompt": "cmd", "paint":"paint","word":"winword", "excel":"excel", "chrome":"chrome","vscode":"code","powerpoint":"powerpnt" }

def openappweb (query):
    speak("Launching, sir")
    if ".com" in query or ".org" in query or ".de" in query :
        query = query.replace("open", "")
        query = query.replace("jarvis", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start{dictapp}")

def closeappweb(query):
    speak("Closing, sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "3 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "4 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    
    else:
        keys = list(dictapp.keys())
        for app in keys:
            for app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")