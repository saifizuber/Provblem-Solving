import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from email.mime import audio
from logging.config import listen
from tkinter import E
import webbrowser
import random
import os
import traceback
from AppOpener import run
import shutil


listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def greet():
    hour = int(datetime.datetime.now().hour)
    if (hour>=0 and hour<12):
        talk('Good Morning  !')
    
    elif(hour>=12 and hour<18):
        talk('Goodafter !')
        
    elif(hour>=18):
        talk('Goodevening !')
         
    talk(" I am Patrick ")


def wishing():
    hour = int(datetime.datetime.now().hour)
    if (hour>=0 and hour<12):
        talk('Good Morning Sir !')
    
    elif(hour>=12 and hour<18):
        talk('Goodafter sir!')
        
    elif(hour>=18):
        talk('Goodevening  sir!')


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Patrick' in command:
                command = command.replace('Patrick', '')
                print(command)
    except:
        pass
    return command


def run_Patrick():
    greet()
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%d /%m /%y')
        print(date)
        talk('Todays date is ' + date)
        
    elif 'wikipedia' in command:
        person = command.replace('wikipedia', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    
    elif 'open youtube' in command:
        webbrowser.open("youtube.com")
            
    elif 'open google' in command:
        webbrowser.open("google.com")

    elif 'open whatsapp' in command:
        webbrowser.open("https://web.whatsapp.com/")

    elif 'open flipkart' in command:
        webbrowser.open("https://www.flipkart.com/")

    elif "show me electronics item" in command:
        webbrowser.open("https://www.flipkart.com/search?q=eletronics%20product&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")   

    elif 'show me sports car photos' in command:
        webbrowser.open("https://www.google.com/search?q=sports+car+photos&sxsrf=ALiCzsaFVE1u7VdZOxtL5SVdPSw4IjStFQ:1669305181537&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjq1veylsf7AhUBT2wGHVnnCQ4Q_AUoAXoECAIQAw&biw=1536&bih=746&dpr=1.25")

    elif "my asus" in command:
        run("MyASUS")

    elif "open teams" in command:
        run("Microsoft Teams(work or school)")

    elif "open search engine" in command:
        run("Microsoft Edge")

    elif "open Brave engine" in command:
        run("Brave")    

    elif "open notes" in command:
        run("Notepad")
        
        

    elif 'morning' or 'afternoon' or 'evening' in command: 
        wishing()
    #elif 'desktop music' in command:
            #music_dir = 'C:\\Users\TH. HIMANSHU SINGH\Music'
            #songs = os.listdir(music_dir)
            #print(songs)
            #random.shuffle(songs)    
            #os.startfile(os.path.join(music_dir, songs[0]))
    #elif 'exit' or 'close' in command:
        #return 0
    else:
        talk('Please say the command again.')


while True:
    run_Patrick()



    