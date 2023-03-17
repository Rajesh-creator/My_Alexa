import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)


def talk(text):
    alexa.say(text)
    alexa.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace('alexa', '')

    except:
        pass
    return command


def run_alexa():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is: ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing...' + song)
        pywhatkit.playonyt(song)
    elif "information" in command:
        look_for = command.replace('information', '')
        info = wikipedia.summary(look_for, 3)
        talk(info)
    elif "joke" in command:
        talk(pyjokes.get_joke())
    elif "date" in command:
        talk("Sorry vaiya, I'm on another relationship")
    else:
        talk("Sorry, I didn't understand but i am going to search it for you")
        pywhatkit.search(command)


while True:
    run_alexa()
