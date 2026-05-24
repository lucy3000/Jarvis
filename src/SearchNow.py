import speech_recognition
import pytest
import pywhatkit
import webbrowser
import wikipedia
import pyttsx3
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

query = takeCommand().lower()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis", "")
        query = query.replace("google search", "")
        query = query.replace("google", "")
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 1)
            speak(result)

        except:
            speak("NO speakable output available")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found for your search!")
        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        query = query.replace("jarvis", "")
        web = "https://www.youtube.com/results\search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak ("Done, sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching form Wikipedia ...")
        query = query.replace("wikipedia", "")
        query = query.replace("search wikipedia", "")
        query = query.replace("jarvis", "")
        results = wikipedia.summary(query, sentences = 2)
        speak("According to wikipedia..")
        print(results)
        speak(results)