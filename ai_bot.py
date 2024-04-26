import random
import datetime
import pyttsx3
import requests
import speech_recognition as sr


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')

engine.setProperty('rate', rate - 25)

user1 = ['hello i want to book appointment','appointment please']
ai_bot1 = ['sure just give me a second']
user2 = ['ok','sure','continue']
user3 = ['12 am','1 am','2 pm','1:00 p.m.','2:00 p.m.']
ai_bot3 = ['please give me your name']
user4 = ['vivek','vinit','yash','Vivek','Vinit','Yash']
ai_bot4 = ['please give your phone number']
user5 = ['6363008426','9955464534']
ai_bot5 = ['Awesome. I have you set up for that time. To cancel or reschedule please call us again. See you soon.']
engine.say('Hello, thanks for calling Dr. Archer’s office. How may I assist you today?')
engine.runAndWait()
name = ""
phone = ""
time = ""
while True:
    now = datetime.datetime.now()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tell me something:")
        audio = r.listen(source)
        try:
            print("You said:- " + r.recognize_google(audio))
            # engine.say("Good")
            engine.runAndWait()
        except sr.UnknownValueError:
            print("Could not understand audio")
            engine.say('I didnt get that. Rerun the code')

            engine.runAndWait()
    if r.recognize_google(audio) in user1:
        random_greeting = random.choice(ai_bot1)
        print(random_greeting)
        engine.say(random_greeting)
        engine.runAndWait()
    elif r.recognize_google(audio) in user2:
        res = 'Please select from these time slots:'
        r = requests.get("http://127.0.0.1:8000/get_all_available_slots")
        times = r.json()
        print(times)
        for i in range(len(times)):
            if i< len(times) - 1:
                res += times[i] + " , "
            else:
                res += times[i] + " . "
        res += 'Please select any one from them.'
        engine.say(res)
        engine.runAndWait()
        print(res)
    elif r.recognize_google(audio) in user3:
        time = r.recognize_google(audio)
        res = random.choice(ai_bot3)
        engine.say(res)
        engine.runAndWait()
        print(res)
    elif r.recognize_google(audio) in user4:
        name = r.recognize_google(audio)
        res = random.choice(ai_bot4)
        engine.say(res)
        engine.runAndWait()
        print(res)
    elif "".join(r.recognize_google(audio).split()) in user5:
        phone = "".join(r.recognize_google(audio).split())
        url = 'http://127.0.0.1:8000/schedule-appointment/'
        myobj = {'patient_name': name,'patient_contact':phone,'time':time}
        print(myobj)
        x = requests.post(url, params=myobj)
        print(x.text)
        res = x.text
        engine.say(res)
        engine.runAndWait()
        print(res)
        res = random.choice(ai_bot5)
        engine.say(res)
        engine.runAndWait()
        print(res)
    else:
        engine.say('Invalid input')
        engine.runAndWait()
        print("Invalid input")