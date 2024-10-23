import pyttsx3

engin = pyttsx3.init()
engin.setProperty('rate',150)
engin.setProperty('voice', engin.getProperty('voices')[0].id)
Say=input("Enter something to say : ")
engin.say(Say)
engin.runAndWait()