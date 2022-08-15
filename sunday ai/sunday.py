import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import mediapipe as mp
from fuzzywuzzy import fuzz

def listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        command = r.recognize_google(audio , language="en-in")
        print(f"you said : {command}")

    except:
        return ""

    command = str(command)
    return command.lower()

engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 160)     # setting up new voice rate
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id) #1 for female and 0 for male

def talk(text):
    engine.say(text)
    engine.runAndWait()

def greeting(command): 
    if('hello' in command or 'hi' in command or 'hey' in command ):
        c1 = "hello "
        return c1   
    else:
        return ""

def ans(command):
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    
    elif '001' in command or 'master code' in command:
        talk("i will activate master mode but ")
        talk("prove me you are nikhil     tell me the password")
        c2 ="incorrect"
        password = listen()
        
        f = open("masterpassword.txt","r")
        s = f.readlines()        
        if(s[0]==password):
            c2 = "welcome sir"

        f.close()
        return c2

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'do you know ' in command:
        person = command.replace('do you know ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info) 
        return ""   
    elif 'are you single' in command:
        c2 = 'I am in a relationship with wifi'
        return c2

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'nikhil' in command:
        print("I only know that nikhil is my god haa haa haa haaaa")
        talk('I only know that nikhil is my god haa haa haa haaaa')

    elif 'who created you' in command:
        print("nikhil kherajani is my god because he created me haa haa haa haa")
        talk('nikhil kherajani is my god because he created me haa haa haa haa')

    else:
        f = open("sunday.txt","r")
        s = f.readlines()
        i=0
        '''ratioss = [None] * len(s)
        while(i<len(s)):
            y = s[i].split(" ans")
            Token_Set_Ratio = fuzz.token_set_ratio(command,y[0])
            ratioss[i] = Token_Set_Ratio 
            i = i + 1 

        max_item = max(ratioss)
        print(ratioss)
        k = [index for index, item in enumerate(ratioss) if item == max_item]
        x = s[k[0]].split("ans ")
        f.close()
        #return x[1]'''

        print("sorry i don't know could you please tell me the ans") 
        talk("sorry i don't know could you please tell me the answer")
        commandans = listen()
        f = open("sunday.txt" , "a")
        f.write(command  +" ans " +commandans + "\n")
        f.close()
        return ""

def courtesy(command):
    if 'please' in command or 'could you please' in command:
        c3 = "and there no need to say please :-) "
        return c3 
    else:
        return ""

def relationship(command):
    if 'dude' in command:
        c3 = "and yes i am not your dude   ok"
        return c3 
    elif 'bro' in command:
        c3 = "and yes i am not your bro   ok"
        return c3 

    elif 'buddy' in command:
        c3 = "and yes i am not your buddy   ok"
        return c3     

    elif 'bhai' in command:
        c3 = "and yes i am not your bhai   ok"
        return c3 

    else:
        return ""

def run_sunday():

    command = listen()
    z=0
    ''' c1=None
    c2=""
    c3=""
    c4="" '''
    c1 = greeting(command)
    c2 = ans(command)
    c3 = courtesy(command)
    c4 = relationship(command)
    if 'bye' in command:
        print('bye')
        z=1
        return z   

    if(len(c1) != 0 or len(c2) != 0 or len(c3) != 0 or len(c4) != 0 ):
        c5 = c1 + c2 + c3 + c4
        print(c5)
        talk(c5)
    return ""   

print("hello i am sunday")
talk("hello i am sunday")
while(1):
    z= run_sunday()
    if(z==1):
        break
