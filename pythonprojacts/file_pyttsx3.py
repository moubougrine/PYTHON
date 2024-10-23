import pyttsx3

song=pyttsx3.init()
with open('C:\\Users\\ABDELMOUGHIT\\Desktop\\pythonprojacts\\exampl.txt', 'r') as file:

    te=file.read()

song.setProperty('rate',150)
song.say(te)
song.runAndWait()