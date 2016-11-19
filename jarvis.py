import speech_recognition
#import pyttsx
import os
import time

#speech_engine = pyttsx.init('sapi5') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
#speech_engine.setProperty('rate', 150)

#def speak(text):
	#speech_engine.say(text)
	#speech_engine.runAndWait()

recognizer = speech_recognition.Recognizer()


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
