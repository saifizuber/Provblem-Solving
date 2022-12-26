from email.mime import audio
from logging.config import listen
from tkinter import E #to GUI 
import pyttsx3 #text to speech convert
import subprocess #to go system on and off or in sleepmode
import pywhatkit #to open and search queries on application
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import wolframalpha  #to find results from userquestions of mathematics
import os
import random
import selenium 
import winshell
import pyjokes
import shutil #to create file in read or write mode
import json #to get weather details
import feedparser
import smtplib
import requests #to get weather details
from twilio.rest import TwilioClient
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

NEWS_API_KEY=" f506c90992f2462f97464c2f21711224"

#import speechRecognition as sr

engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[3].id)
engine.setProperty('voices',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
          
def wishing():
    hour = int(datetime.datetime.now().hour)
    if (hour>=0 and hour<12):
        speak('Good Morning sir')
    
    elif(hour>=12 and hour<18):
        speak('Goodafter sir!')
        
    elif(hour>=18):
        speak('Goodevening sir !')
 
def getName():
    global username
    speak("Can I please know your name?")
    username = takeuserinput()
    print("Name:",username)
    speak("I am glad to know you!")
    columns = shutil.get_terminal_size().columns
    speak("How can i Help you, ")
    speak(username)
        
def greet():
    hour = int(datetime.datetime.now().hour)
    if (hour>=0 and hour<12):
        speak('Good Morning Naman Sir !')
    
    elif(hour>=12 and hour<18):
        speak('Goodafter Naman !')
        
    elif(hour>=18):
        speak('Goodevening Naman !')
         
    speak(" I am Patrick , Your new ai based Desktop assistant.  How can i help you today ? ")
    
def send_whatsapp_message(number, message):
    pywhatkit.sendwhatmsg_instantly(f"+91{number}", message)

def takeuserinput():
    #it takes microphone input from the user and returns string output
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.......')
        r.pause_threshold = 0.8
        audio = r.listen(source)
        
    try:
        print('Recognizing..... ')
        userinput = r.recognize_google(audio,language='en-in')
        print(f'user said : {userinput}\n ')
        
    except Exception as e:
        #print(e)
        print('Say that again please ')
        return "None"
    return userinput 

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

def sendEmail(to, content):
    print("Sending mail to ", to)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    #paste your email id and password in the respective places
    server.login('namanmotla@gmail.com', '') 
    server.sendmail('your email id', to, content)
    server.close()
    
def getWeather(city_name):
    #cityName=place.get() #getting input of name of the place from user
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?" #base url from where we extract weather report
    url = baseUrl + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + cityName  
    response = requests.get(url)
    x = response.json()

    #If there is no error, getting all the weather conditions
    if x["cod"] != "404":
        y = x["main"]
        temp = y["temp"]
        temp-=273 
        pressure = y["pressure"]
        humidity = y["humidity"]
        z = x["weather"]
        description = z[0]["description"]
        info=(" Temperature= " +str(temp)+"°C"+"\n atmospheric pressure (hPa) ="+str(pressure) +"\n humidity = " +str(humidity)+"%" +"\n description = " +str(description))
        print(info)
        speak("Here is the weather report at")
        speak(city_name)
        speak(info)
    else:
        speak(" City Not Found ")
paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'discord': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}
def open_notepad():
    os.startfile(paths['notepad'])
def open_discord():
    os.startfile(paths['discord'])
def open_cmd():
    os.system('start cmd')
def open_camera():
    subprocess.run('start microsoft.windows.camera:', shell=True)
def open_calculator():
    subprocess.Popen(paths['calculator'])
        
def get_latest_news():
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]
           
if __name__ =="__main__":
    greet()
    while True:
        userinput = takeuserinput().lower()
        mymusic = userinput
        
        if 'wikipedia' in userinput:
            speak('Serarching Wikipedia.......')
            userinput  = userinput.replace('wikipedia', "")
            result = wikipedia.summary(userinput,sentences =2)
            speak('According to Wikipedia ')
            print(result)
            speak(result)
            
        elif 'open youtube' in userinput:
            webbrowser.open("youtube.com")
            
        elif 'open google' in userinput:
            webbrowser.open("google.com")
        
        elif 'play music' in userinput :
            music_dir = 'C:\\Users\\naman\\Desktop\\music'
            songs = os.listdir(music_dir)
            print(songs)
            random.shuffle(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            
                
        elif 'how are you' in userinput or 'how have you been' in userinput :
                speak("I am doing Excellent . Just got a new home in your PC.")
            
        elif 'what are you doing' in userinput:
                speak("I am here speaking to you. That's what I am doing")
    
        elif 'what am i doing' in userinput:
                speak("You tell me. My guess is you are speaking to me")
        
        elif 'how is life' in userinput or 'how is your life' in userinput:
                speak("Life in the silicon world is amazing")
        
        elif 'where do you live' in userinput or 'where do you stay' in userinput or 'where is your home' in userinput \
                    or 'what is your address' in userinput:
                speak('I live in the silicon world. Be born next time as a software. Then you can come live with me too')
        
        elif 'whom am I speaking to' in userinput:
                speak("You are speaking to Patrick ")
        
        elif 'who created you' in userinput or 'who made you' in userinput or 'who is your creator' in userinput or \
                    "who's creation are you" in userinput or 'who has made you' in userinput or \
                    'who has created you' in userinput:
                speak('I was created by Naman  with the helpful suggestions from Himanshu and Zubair  which helped in how I turned out to be.')
        
        elif 'your birthday' in userinput or 'when were you created' in userinput or 'when were you born' in userinput:
                speak('I am a work in progress always.')
        
        elif 'what is your name' in userinput or 'what should I call you' in userinput or \
                    "what's your name" in userinput:
                speak("I am Patrick")
        
        elif 'to whom do you belong' in userinput or 'who is your owner' in userinput:
                speak("I am owned and copyrighted by "+username)
        elif "will you be my gf" in userinput or "will you be my bf" in userinput:
            speak("I'm not sure about that, may be you should give me some time")
        elif "i love you" in userinput:
            speak("Thank you! But, It's a pleasure to hear it from you.")
        elif 'joke' in userinput:
            speak(pyjokes.get_joke())
            
        elif 'mail' in userinput:
            try:
                speak("Whom should I send the mail")
                to = takeuserinput()
                speak("What is the body?")
                content = takeuserinput()
                sendEmail(to, content)
                speak("Email has been sent successfully !")
            except Exception as e:
                    print(e)
                    speak("I am sorry, not able to send this email")

        elif 'exit' in userinput or 'Thankyou patrick' in userinput:
            speak("Thanks for giving me your time")
            exit()

        elif "weather" in userinput:
            speak(" Please tell your city name ")
            print("City name : ")
            cityName = takeuserinput()
            getWeather(cityName)

        elif "what is" in userinput or "who is" in userinput:
            
            client = wolframalpha.Client("API_ID")
            res = client.query(userinput)

            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")

        elif 'search' in userinput:
            userinput = userinput.replace("search", "")
            webbrowser.open(userinput)

        elif 'news' in userinput:
            speak(f"I'm reading out the latest news headlines, sir")
            speak(get_latest_news())
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_latest_news(), sep='\n')
        
        elif "don't listen" in userinput or "stop listening" in userinput:
            speak("for how much time you want to stop me from listening userinputs")
            a = int(takeuserinput())
            time.sleep(a)
            print(a)
            
        elif 'shutdown system' in userinput:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

        elif "restart" in userinput:
            subprocess.call(["shutdown", "/r"])

        elif "sleep" in userinput:
            speak("Setting in sleep mode")
            subprocess.call("shutdown / h")
        elif "open notepad" in userinput:
            speak("Opening notepad sir")
            open_notepad()
        elif "open discord" in userinput:
            speak("Opening discord sir")
            open_discord()
        elif "open cmd" in userinput or "open command prompt" in userinput:
            speak("Opening command prompt sir")
            open_cmd()
        elif "camera" in userinput:
            speak("Opening camera sir")
            open_camera()
        elif "calculator" in userinput:
            speak("Opening calculator sir")
            open_calculator()
        
        elif "advice" in userinput:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            print(advice)

        elif "write a note" in userinput:
            speak("What should i write, sir")
            note = takeuserinput()
            file = open('Patrick.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeuserinput()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
                
        elif 'play youtube' in userinput:
            song = userinput.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in userinput:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            speak('Current time is ' + time)
        elif 'date' in userinput:
            date = datetime.datetime.now().strftime('%d /%m /%y')
            print(date)
            speak('Todays date is ' + date)
                
                
        elif 'message ' in userinput or 'whatsapp' in userinput:
            speak('whom u want to send message')
            number = takeuserinput()
            speak('what message u want to send ')
            message= takeuserinput()
            send_whatsapp_message(number, message)
            speak('sending message')
            print("Successfully Sent!")

            
            
        else:
            speak("Sorry, I am not able to understand you")
            
            
        
            
        
                
        
                
                
        
                
                
                
                
            
            
                
            
                
            
                
            
            
            
        
    