import time 
import pyttsx3

i = input("Enter your reminder : ")
o = int(input("set the reminder interval in seconds : "))
l = pyttsx3.init()
while True:
    time.sleep(o)
    l.setProperty('rate',150)
    l.say(i)
    l.runAndWait()