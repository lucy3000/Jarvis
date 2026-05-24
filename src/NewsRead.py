import requests
import json
import pyttsx3
from jarvis_voice import speak

def latestnews():
    api_dict = {
        "science": "https://www.sciencenews.org/",
        "technology": "https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=API_KEY"
    }

    speak("which field news do you want, sir. You can choose between [science], [technology]")
    field = input("Type field news that you want: ")

    url = None
    for key, value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(f"url was found: {url}")
            break

    if url is None:
        speak("url not found")
        return

    news = requests.get(url).json()
    arts = news['articles']
    for article in arts:
        title = article['title']
        speak(title)
        print(title)

        news_url = article["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to continue] and [press 2 to stop]: ")
        if str(a) == "2":
            break

    speak("that is all")

if __name__ == "__main__":
    latestnews()
