import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)



def speak(audio):
     engine.say(audio)
     engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning boss")
    elif hour>12 and hour<16:
        speak ("good afternoon boss")
    else:
        speak("good evening boss") 
    speak ("i am jarvis please tell me how may i help you")    

def takecommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=0.5
        audio =r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said : {query}\n")
    except Exception as e:
        print("say that again please") 
        return "None"
    return query        


    



if __name__ == '__main__':
    wishme()
    while True:
        query= takecommand().lower()


        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)    
            speak("according to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")    
        elif 'open google' in query:
                webbrowser.open("google.com")
        elif 'open facebook' in query:
                webbrowser.open("facebook.com")
        elif 'who is your boss' in query:
            speak("sajal gupta is my boss")
        

    
            
                


        elif 'shutdown' in query:
            exit()    
            
                   


        elif 'play music' in query:
            musicf='S:\Music'
            songs=os.listdir(musicf)
            print(songs)
            os.startfile(os.path.join(musicf,songs[0]))
