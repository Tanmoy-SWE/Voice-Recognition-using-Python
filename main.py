import speech_recognition as sr
from pathlib import Path
recogniser = sr.Recognizer()
try :
    #Firstly it needs to listen what the user says
    with sr.Microphone() as voice :
        print("I'm listening to you boss.....")
        voiceSound = recogniser.listen(voice)
        #Calling the google API to convert voice to text
        VoiceString = recogniser.recognize_google(voiceSound)
except :
    pass
VoiceString = VoiceString.upper()
print(VoiceString)
#Creating a text file to store the texts of the audio
fh = open("TextFromAudio.txt", 'w')
#Writing the Voice Texts in the file
fh.write(VoiceString)
