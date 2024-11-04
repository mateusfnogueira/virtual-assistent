import speech_recognition as sr
import re

import pyttsx3

name = ''

while(True):
  mic = sr.Recognizer()

  with sr.Microphone() as source:
    engine = pyttsx3.init()
    engine.setProperty('voice', "com.apple.speech.synthesis.voice.luciana")
    mic.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = mic.listen(source)
    try:
      phrase = mic.recognize_google(audio,language='pt-BR')
      if(re.search(r'\b' + 'ajudar' + r'\b', format(phrase))):
        engine.say("Com o que você precisa de ajuda")
        engine.runAndWait()
        print('Do you want a help for?')
      
      elif(re.search(r'\b' + 'meu nome é' + r'\b', format(phrase))):
        t=re.search('meu nome é (.*)', format(phrase))
        name = t.group(1)
        print("Your name is " + name)
        engine.say("Muito prazer " + name)
        engine.runAndWait()

      print("you said: " + phrase)

    except sr.UnknownValueError:
      print('Unknown Error')
  