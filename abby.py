import pyttsx3
#import pyaudio
import  datetime
from datetime import datetime 
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id)


#functions 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")
    elif hour>= 12 and hour < 16:
        speak("Good Afternoon")
    else:
        speak('Good Evening')
    speak("Nice to see you! I am Abby, how may i be of your service")

def takeCommand():
    #audio input
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....!')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
       #print(e)
       print('Pardon me for interruption, can you say that again')
       return "None"
    return query

#def sendEmail(to ,content):   
    # server = smtplib.SMTP('smtp.gmail.com',587)
    # server.ehlo()
    # server.starttls()
    # server.login("youremail@gmail.com", "yourpassword")
    # server.sendmail('youremail@gmail.com',to , content)
    # server.close()

    
    

#main function
if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        #logic for exec of task

        if "wikipedia" in query:
            speak("Searching Wikipedia..")
            query = query.replace("wikepedia", "")
            results = wikipedia.summary(query, sentences= 5)
            speak("According to Wikipedia")
            speak(results)

        
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open stack' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            speak(f'Current time is {strTime}')

        elif 'open code' in query:
            codepath= "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        elif 'open android studio' in query:
            studiopath= "C:\\Program Files\\Android\Android Studio\\bin\\studio64.exe"
            os.startfile(studiopath)
        
        #this will work only if sendEmail func is uncommented
        elif 'send email' in query:
            try:
                speak('what should i type?')
                content = takeCommand()
                to = "reciever@gmail.com"
                #sendEmail(to,content)
                speak('email has been sent')
            except Exception as e:
                print(e)
                speak('Pardon me for interrruption, email could not be sent')

        


