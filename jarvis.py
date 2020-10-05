import speech_recognition
#import pyttsx
import os
import time
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import smtplib
#from ex import * weather module made by me..
import sys 
import weather_forecast as wf

#speech_engine = pyttsx.init('sapi5') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
#speech_engine.setProperty('rate', 150)

#def speak(text):
	#speech_engine.say(text)
	#speech_engine.runAndWait()

recognizer = speech_recognition.Recognizer()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  



def listen():
	with speech_recognition.Microphone() as source:
		#recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)

	try:
		return recognizer.recognize_sphinx(audio)
		# or: return recognizer.recognize_google(audio)
	except speech_recognition.UnknownValueError:
		print("Could not understand audio")
	except speech_recognition.RequestError as e:
		print("Recog Error; {0}".format(e))

	return ""

#speak("Say something!")
#speak("I heard you say " + listen())
#a=listen()
#print a


# List of voice options available in Say command
Female_Voices = ['Agnes', 'Kathy', 'Princess', 'Vicki', 'Victoria']
 
Male_Voices = ['Alex', 'Bruce', 'Fred', 'Junior', 'Ralph']
 
Novelty_Voices = ['Albert', 'Bad News', 'Bahh', 'Bells', 'Boing', 'Bubbles',
                  'Cellos', 'Deranged', 'Good News', 'Hysterical', 'Pipe Organ',
                  'Trinoids', 'Whisper', 'Zarvox']
 
all_voices = Female_Voices + Male_Voices + Novelty_Voices




#for voice in all_voices:
#	time.sleep(1)
#	print "Voice is "+voice

def say(text):
	voice='Luciana'
	os.system("say -v "+voice+"  "+text)

def ouvir():
	a="Error"
	try:
		a=listen()
	except:
		print "Error"
	return a
if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak('okay')

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak('okay')

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 
            speak('okay')

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            speak('okay')

         
        elif 'play music' in query:
              webbrowser.open("gaana.com/topcharts")
              speak('okay')

            

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'weather' in query:
           #x=input("Enter the place-")
            #y=input("Enter the Time(24hr)-")
            #z=input("Enter the date(Y-m-d)-")
            wf.forecast(place = 'Mumbai', time=datetime.datetime.now(), date=datetime.now().strftime('%Y-%m-%d'), forecast="daily")
            speak('okay')

	
#say("Bom dia najinha")
say("Bom dia mestre najinha")
say("O que temos para hoje?")
a=ouvir()		
print a
say("Voce disse "+a+"?" )
say("Nao sei o que quer dizer com isso")
say("Posso incluir na base de aprendizado?")
	
a=ouvir()
print a
