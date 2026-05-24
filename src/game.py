import pyttsx3
import speech_recognition
import random
from jarvis_voice import speak

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        try:
            audio = r.listen(source, timeout=4)
        except speech_recognition.WaitTimeoutError:
            print("Timeout occurred while listening.")
            return "None"

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def game_play():
    speak("Let's play Rock Paper Scissors!")
    i = 0
    Me_score = 0
    Com_score = 0

    while i < 5:
        print("Say 'rock', 'paper', or 'scissors'")
        query = takeCommand().lower()
        
        if query == "none":
            speak("I didn't catch that. Please say again.")
            continue
        
        if "finish" in query:
            speak("That was a good game. Goodbye!")
            exit()

        choices = ["rock", "paper", "scissors"]
        com_choose = random.choice(choices)

        if query in choices:
            if query == com_choose:
                speak(f"I chose {com_choose}. It's a tie!")
            elif (query == "rock" and com_choose == "scissors") or \
                 (query == "paper" and com_choose == "rock") or \
                 (query == "scissors" and com_choose == "paper"):
                speak(f"I chose {com_choose}. You win this round!")
                Me_score += 1
            else:
                speak(f"I chose {com_choose}. I win this round!")
                Com_score += 1

            print(f"Score: You {Me_score} - Computer {Com_score}")
            i += 1
        else:
            speak("Invalid choice. Please say 'rock', 'paper', or 'scissors'.")

    speak(f"Final score: You {Me_score}, Computer {Com_score}. Thanks for playing!")

