import pywhatkit
import speech_recognition as sr
import pyttsx3  # python text to speech
import datetime
import wikipedia
import pyjokes

# creating a listener to recognize the user's voice
listener = sr.Recognizer()

# creating an engine for the python to speak to the user
engine = pyttsx3.init()

# creating a female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# alexa speak to the user
def talk(text):
    engine.say(text)
    engine.runAndWait()


talk("Hello, I'm Alexa. What can I do for you?")


# taking the command from the user
def take_command():
    # creating try and except block if the microphone fails
    try:
        # creating the microphone as the source to listen
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            # to convert speech to text using Google api
            command = listener.recognize_google(voice)
            # to check whether the user speaks alexa as the first word
            command = command.lower()
            if "alexa" in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


# running the command
def run_command():
    command = take_command()
    print(command)
    # to play something
    if "play" in command:
        song = command.replace('play', '')
        print("playing" + song)
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        print("current time is " + time)
        talk("current time is " + time)
    elif "what is the date today" in command:
        date = datetime.datetime.now().strftime("%d/%m/%y")
        print("current date is " + date)
        talk("current date is " + date)
    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif "what is a" in command:
        thing = command.replace("what is a", "")
        info_2 = wikipedia.summary(thing, 2)
        print(info_2)
        talk(info_2)
    elif "what is an" in command:
        thing = command.replace("what is an", "")
        info_3 = wikipedia.summary(thing, 2)
        print(info_3)
        talk(info_3)
    elif "what is the" in command:
        thing = command.replace("what is the", "")
        info_4 = wikipedia.summary(thing, 2)
        print(info_4)
        talk(info_4)
    elif "joke" in command:
        talk(pyjokes.get_joke())
    elif "are you single" in command:
        print("Sorry, I'm in a relationship with WiFi")
        talk("Sorry, I'm in a relationship with WiFi")
    else:
        print("Please, tell the command again.")
        talk("Please, tell the command again.")


while True:
    run_command()
