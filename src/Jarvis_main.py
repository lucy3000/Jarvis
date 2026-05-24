"""
Title: KNN
Author: Sophia Wewetzer
Date created: 2024/04/18
Last modified: 
Description: AI assistance (jarvis)
Accelerator: none
"""

#import libaries
import pyttsx3 #text-to-speech libary
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import random
import webbrowser
from plyer import notification
from pygame import mixer
import pyautogui
import pygame
import deezer
from selenium import webdriver
import time
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

for i in range(3):
    a = input("Enter Password to open Jarvis :-")
    pw_file = open("password.txt", "r")
    pw = pw_file.read()
    pw_file.close()
    if (a == pw):
        print("Welcome sir! please speak[Wake up] to load me up")
        break
    elif(i == 2 and a!=pw):
        exit()
    elif(a!=pw):
        print("Try Again")

#from gui import TodoListApp
#TodoListApp()

#jarvis stimme
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
        speak("Sorry, I didn't understand that")
        return "None"
    return query

def get_response_from_gpt(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()


#def for alarm
def alarm(query):
    timehere = open("Alarm.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok, sir, you can call anytime")
                    break
                ########################Jarvis: The Trilogy 2.0##########################
                elif"change password" in query:
                    speak("What is your new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.tx", "w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")

                #schedul my day
                elif "schedule my day" in query:
                    tasks = [] #empty list
                    speak("Do you want to clear older tasks (Please speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt", "w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the number of tasks :-"))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the tasks :-"))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :-"))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the tasks :-"))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                elif "show my schedule" in query:
                    file = open("tasks.txt", "r")
                    content = file.read()
                    file.close()
                    mixer.init()  # Hier wird der Mixer initialisiert
                    #mixer.music.load("notification.mp3")
                    #mixer.music.play()

                    notification.notify(
                        title="My schedule :-",
                        message=content,
                        timeout=15
                    )
                
                elif "check off task" in query:
                    if os.path.exists("tasks.txt"):
                        with open("tasks.txt", "r") as file:
                            tasks = file.read().splitlines()
                        
                        speak("Which task can I tick off?")
                        for i, task in enumerate(tasks, start=1):
                            print(f"{task}")
                        
                        task_to_remove = int(input("Enter the task number to remove: "))
                        
                        if 0 < task_to_remove <= len(tasks):
                            tasks.pop(task_to_remove - 1)
                            with open("tasks.txt", "w") as file:
                                for i, task in enumerate(tasks, start=1):
                                    file.write(f"{i}. {task}\n")
                            print(f"Task {task_to_remove} has been checked off.")
                        else:
                            print("Invalid task number!")
                    else:
                        print("No tasks found! Please schedule your day first.")


                #open app with voice
                elif "open" in query: 
                    query = query.replace("open", "")
                    query = query.replace("jarvis", "")
                    pyautogui.press("super")
                    
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")


                #play rock paper scissor game
                elif "play a game" in query:
                    from game import game_play
                    game_play()

                #screenshot function
                elif "screenshot" in query:
                    import pyautogui
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")
                #photo function
                elif "take a photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("smile")
                    pyautogui.press("enter")


                ###################################################################
                #"small talk"
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak ("that is great")
                elif "how are you" in query:
                    speak ("Perfect sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                
                #own playlist
                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b == 1:
                        webbrowser.open("https://www.youtube.com/watch?v=aezstCBHOPQ")
                    elif b == 2:
                        webbrowser.open("https://www.youtube.com/watch?v=0I647GU3Jsc")   
                    else:
                        webbrowser.open("https://www.youtube.com/watch?v=Ee_uujKuJMI")   
                
                # Dezzer
                elif "play music" in query:
                    # Deezer-Client erstellen (NutzerID = 5226301462)
                    client = deezer.Client(app_id='5226301462')

                    # Playlist abrufen
                    playlist = client.get_playlist('11680653684')

                    # Musik abspielen
                    playlist_url = playlist.link
                    webbrowser.open(playlist_url)
                    
                    
                    # Warte ein paar Sekunden, um sicherzustellen, dass die Seite vollständig geladen ist
                    time.sleep(5)

                    # Suche das Play-Symbol und klicke darauf, um die Wiedergabe zu starten
                    #play_button = driver.find_element_by_class_name('player-controls__button.play')
                    #play_button.click()

                    # Warte eine Weile, damit die Wiedergabe beginnt
                    time.sleep(10)

                    # Schließe den Webdriver
                    #driver.quit()



                #Youtube controller 
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif"volume up" in query:
                    from keyword import volumeup
                    speak("Turning volume up, sir")
                    volumeup()
                elif"volume down" in query:
                    from keyword import volumedown
                    speak("Turning volume down, sir")
                    volumedown()

                #open/close web
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                #search on google, youtube, wikipedia
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                #news function
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

                elif "calculate" in query:
                    from Calculatenumbers import Calc
                    speak("What should I calculate, sir?")
                    query = takeCommand().lower()

                    if query:  
                        print(f"Raw query: {query}") 
                        result = Calc(query)

                        if isinstance(result, str) and result.startswith("Error"):
                            speak(f"Sorry, I couldn't calculate that: {result}")
                            print(f"Error: {result}")
                        else:
                            print(f"The result is: {result}")
                            speak(f"The result is {result}")



                #whatsapp answering per voice
                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()


                #tell temperature/weather
                elif "temperature" in query:
                    search = "temperature in Potsdam"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    
                    temp_element = data.find("div", class_="BNeawe")
                    if temp_element:
                        temp = temp_element.text
                        speak(f"The current {search} is {temp}")
                    else:
                        speak("Sorry, I couldn't retrieve the temperature. Google might have changed its page structure.")

                elif "weather" in query:
                    search = "weather in Potsdam"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")


               # set an alarm
                elif "set an alarm" in query:
                    print("Input time example: 10:10:10")
                    speak("Please set the time")
                    time_input = input("Please tell the time (format: HH:MM:SS) :- ")
                    
                    # Überprüfen, ob die Zeit im richtigen Format eingegeben wurde
                    try:
                        datetime.datetime.strptime(time_input, '%H:%M:%S')
                    except ValueError:
                        speak("Invalid time format. Please enter the time in the format HH:MM:SS.")
                        continue  # Weiter mit der nächsten Iteration der Schleife
                    
                    # Wenn die Zeit im richtigen Format eingegeben wurde, wird der Alarm eingestellt
                    alarm(time_input)
                    speak("Alarm set successfully, sir.")

                #tell the time
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")

                #ausschalten
                elif "finally sleep" or "goodnight" in query:
                    if "finally sleep" in query:
                        speak("Going to sleep, sir")
                        exit()
                    if "goodnight" in query:
                        speak("Good night sir")
                        exit()

                #remember function
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", "")
                    rememberMessage = query.replace("jarvis", "")
                    speak("You told me " + rememberMessage)
                    remember = open("Remember.txt", "w")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt")
                    speak("You told me" + remember.read())

                #shutdown function
                elif "shutdown system" in query:
                    speak("Are you sure you want to shutdown?")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break

                else:
                    response = get_response_from_gpt(query)
                    print(f"Jarvis: {response}")
                    speak(response)