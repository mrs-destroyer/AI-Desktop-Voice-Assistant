import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def wishMe():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning Neha! I'm Zira. How can i help you")
        speak("Good Morning Neha! I'm Zira. How can i help you")        
    elif hour>=12 and hour>18:
        print("Good Afternoon Neha! I'm Zira. How can i help you")
        speak("Good Afternoon Neha! I'm Zira. How can i help you")
    elif hour<=18 and hour>23:
        print("Good Evening Neha! I'm Zira. How can i help you")
        speak("Good Evening Neha! I'm Zira. How can i help you")
    else:
        print("Hurry up! its time to go sleep now ")
        speak("Hurry up! its time to go sleep now")


def time():
        strTime = datetime.datetime.now().strftime("%H:%M:%S") 
        print(strTime)  
        speak(f"yeah , the time is {strTime}") 
def date():
        strDate = datetime.datetime.now().strftime("%D:%M:%Y") 
        print(strDate)  
        speak(f"yeah , the date is {strDate}")  

def honor():
    print("Thanks Neha , its means a lot for me")
    speak("Thanks Neha , its means a lot for me")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognising....")
        query = r.recognize_google(audio, language='en=pak')
        print(f"you said: {query}\n")
    except Exception as e:
        print(e)
        print("I can't understand please Say that again ...")
        speak("I can't understand please Say that again ...")
        return"None"
    return query  

if __name__ == "__main__": 
    print("Welcome Neha! Say [wake up] to load me")
    while True:


        query = takeCommand().lower()
        if 'wake up' in query:    
            wishMe()
        elif'the time' in query:
            time()
        elif 'the date' in query:
            date()
        elif'well done' in query:
            honor()
        elif 'wikipedia' in query:
            print("Wait i am searching wikipedia...")
            speak("Wait i am searching wikipedia...")
            query= query.replace("wikipedia"," ")
            results = wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)       
        elif'open google' in query:
            print("Yeah google is open now")
            speak("Yeah google is open now")
            webbrowser.open("google.com") 
            speak("Done!")     
        elif'open youtube' in query:
            print("Yeah youtube is open now")
            speak("Yeah youtube is open now")
            webbrowser.open("youtube.com") 
            speak("Done!") 
        elif'open firefox' in query:
            print("Yeah firefox is open now")
            speak("Yeah firefox is open now")
            webbrowser.open("Firefox.com")  
            speak("Done!")          
        elif'play music' in query:
            print("Yeah music is start ")
            speak("Yeah music is start ")
            music_dir = 'D:\\jarvis'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[3]))
            speak("Done!") 
        elif'pause' in query:
            pyautogui.press("k")
            print("Yeah the video is paused")
            speak("Yeah the video is paused ")   
        elif'play' in query:
            pyautogui.press("k")
            print("the video is play")
            speak("the video is play") 
        elif'mute' in query:
            pyautogui.press("m")
            print("the video is muted")   
            speak("the video is muted")     
        elif'open AI Quiz' in query:
            print("Yeah AI Quizzer is open now")
            speak("Yeah AI Quizzer is open now")
            AIQuizzerPath = "C:\\Program Files (x86)\\Ai Quizzer\\aiquizzer.exe"
            os.startfile(codePath)
            speak("Done!") 
        elif'open VS code' in query:
            print("Yeah VS code is open now")
            speak("Yeah VS code is open now")
            VScodePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            os.startfile(codingPath)   
            speak("Done!") 
        elif'open github' in query:
            print("Yeah github is open now")
            speak("Yeah github is open now")
            githubPath = "C:\\Users\\hp\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"
            os.startfile(githubPath)
            speak("Done!") 
        elif"open" in query:
            query = query.replace("open","")
            query = query.replace("Zira","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter") 
            speak("Done!")   
        elif'goodbye' in query:
            print("GoodBye Neha, Have a Nice day!")
            speak("GoodBye Neha, Have a Nice day!")
            exit()  
        elif'good night' in query:
            print("Good Night Neha! Have a sweet dreams")
            speak("Good Night Neha! Have a sweet dreams") 
            exit()        
        
        

