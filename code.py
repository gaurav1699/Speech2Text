import speech_recognition as sr
import pyaudio
from pydub import AudioSegment
from os import path
import sys
import os
import datetime

def banner():
    print('''
         ____                       _     ____ _____         _   
        / ___| _ __   ___  ___  ___| |__ |___ \_   _|____  _| |_ 
        \___ \| '_ \ / _ \/ _ \/ __| '_ \  __) || |/ _ \ \/ / __|
         ___) | |_) |  __/  __/ (__| | | |/ __/ | |  __/>  <| |_ 
        |____/| .__/ \___|\___|\___|_| |_|_____||_|\___/_/\_\\__|
              |_|                                                

                  ''')
    return



r= sr.Recognizer()
r.energy_threshold = 4000


banner()
print("====================================================================")
p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(0, numdevices):
    if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
        print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))
print("....................................................................")        

with sr.Microphone() as source:
    global name
    print("Tell me your name");
    print("....................................................................") 
    r.pause_threshold = 0.8
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    
    try:
        name=r.recognize_google(audio)  
        
    except:
        print("Could not understand audio")
        
filename=datetime.datetime.now().strftime(name+"-%d-%m-%Y-%H-%M-%S"+".txt")
convertedTextFile=os.path.splitext(filename)[0]

# output to textfile
def saveToFile(text):
   file=open("textfiles/"+convertedTextFile,"w")
   file.write(text)
   file.close()
   print("------------------------------------------------------------------")
   print("Text file is saved")
   
   
#speech to text   
with sr.Microphone() as source:
    print("Hi "+name + " Please say something");
    print("------------------------------------------------------------------")
    #audio = r.record(source,duration=30)
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source) 
    print("Time is up " + name + " Wait for the text: ")
    print("------------------------------------------------------------------") 
    try:
         # for testing purposes, we're just using the default API key
        print("You said " + r.recognize_google(audio)) #language="hi-IN"
        saveToFile(r.recognize_google(audio))
        #saving audio file  
        with open("audiofiles/"+convertedTextFile+".mp3", "wb") as f:
            f.write(audio.get_wav_data())
            print("------------------------------------------------------------------")
            print("audio file is saved ")

    except:
        print("Could not understand audio")




# write audio to a WAV file if you want another file format 
#just change the extension to that format such as AIFF,FLAC,RAW
    
    
    
#---Transcribe an Audio File----
#audiofilename='female.wav'
#---convert  mp3 to wav
# sound = AudioSegment.from_mp3("demo.mp3")
# sound.export("demo.wav", format="wav")

#currentAudioClip = sr.AudioFile("audiosource/"+audiofilename)
#with currentAudioClip as source:
#    audio = r.record(source)

#r.recognize_google(audio)
#print(r.recognize_google(audio))
#saveToFile(r.recognize_google(audio))

