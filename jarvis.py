import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = aa.Recognizer()
machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    global instruction
    try:
        with aa.Microphone() as origin:
            print("Listening...")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "jarvis" in instruction:
                instruction = instruction.replace('jarvis', '')
                print(instruction)
                return instruction
    except Exception as e:
        print("Error:", str(e))
        talk("Sorry, I did not catch that.")
    return ""

def play_jarvis():
    while True:
        instruction = input_instruction()
        if instruction:
            print(instruction)
            if "play" in instruction:
                song = instruction
                talk("Playing " + song)
                pywhatkit.playonyt(song)
            elif 'time' in instruction:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk('Current time is ' + time)
            elif 'date' in instruction:
                date = datetime.datetime.now().strftime('%d /%m /%Y')
                talk("Today's date is " + date)
            elif 'how are you' in instruction:
                talk("I am good, what about you?")
            elif 'what is your name' in instruction:
                talk("I am Jarvis. What can I do for you?")
            elif 'who is' in instruction:
                human = instruction.replace('who is', "")
                info = wikipedia.summary(human, 2)
                print(info)
                talk(info)
            else:
                talk("Please repeat.")

play_jarvis()
