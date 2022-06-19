#Daily news
#news api
import requests
import json
#relevant headlines through APi then download pywin32 package
def speak(str):
     from win32com.client import Dispatch
     speak = Dispatch("SAPI.SpVoice")
     speak.Speak(str)

if __name__ == '__main__':
    speak("News for today")
    url=" you an add path API here"
    news = requests.get(url).text   #txt dene ke liye
    news_dict = json.loads(news)    #yha string hgyi pyhton object mai
    arts= news_dict['articles']
    for i, article in enumerate(arts):
        if article[-1]:
            speak("hers you last news ")
            print(article[i]['title'])
            speak(article[i]['title'])
        else:
            print(article[i]['title'])
            speak(article[i]['title'])
        speak(("moving to next news...listen carefully"))
    speak("Thanks for listening")
