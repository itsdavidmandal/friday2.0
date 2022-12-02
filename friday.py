import speech_recognition as sr #python speech recognition
import pyttsx3 # python text to speech packages
import pywhatkit # used for youtube automation
import datetime # used to show the date and time
import wikipedia
import pyjokes

listener = sr.Recognizer()


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print(" listening ....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'friday' in command:
                command = command.replace('friday', '')



    except:
        pass
    return command


def run_friday():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%S:%p')
        print(time)
        talk('current time is ' + time)

    #elif 'wikipedia' in command:
       # person = command.replace('wikipedia', '')
        #info = wikipedia.summary(person, 1)
        #print(info)
        #talk(info)#
    elif 'date' in command:
        talk('not interested')
    elif 'are you single' in command:
        print('>.<')
        talk('i am in relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('please say the command again')
while True:
    run_friday()
