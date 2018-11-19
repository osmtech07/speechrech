import pyaudio
import wave
import speech_recognition as sr
import subprocess
from commads import Commander

running = True
cmd = Commander()
def say(text):
    subprocess.call('say ' + text, shell=True)

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()


r = sr.Recognizer()
def initSpeech():
    global running
    print("Listening....")

    play_audio("./audio/Alesis.wav")

    with sr.Microphone() as source:
        print("Say something...")
        audio= r.listen(source)

    play_audio("./audio/Alesis.wav")

    command = ""
    try:
        command = r.recognize_google(audio)
    except:
        print("Could not understand you...")
    
    print("Your command")
    print(command)
    if command in ['quit', 'exit', 'cancel']:
        running = False
    
    cmd.discover(command)
    #say("You said"+command)

while running ==True:
    initSpeech()