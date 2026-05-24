import pyttsx3

def speak(text):
    # Initialisierung des Text-to-Speech-Engine
    engine = pyttsx3.init()

    # Festlegen der Stimme auf eine männliche Stimme in englischer Sprache
    engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")

    # Einstellungen für Geschwindigkeit und Tonhöhe
    engine.setProperty("rate", 192)  # Geschwindigkeit anpassen 
    engine.setProperty("pitch", 400)   # Tonhöhe anpassen 

    # Sprechen des übergebenen Textes
    engine.say(text)
    engine.runAndWait()