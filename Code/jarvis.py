import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def run_personal_assisiternt():
    wishMe()
    commond = takeCommand()
   

def wishMe():
    
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning!")

    elif hour>=12 and hour <18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")  

    speak("I am your Virtual Assistent! How may I help you") 
      

def takeCommand():



    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognitiion....")
        query = r.recognize_google(audio, Language='en-in')
        print(f"User said: {query}\n")

        
    except Exception as e:
        #print(e)
        print("Say that again please....")
        return "None"
    return query 



if __name__=="__main__":
    wishMe()
    command = takeCommand()
    

