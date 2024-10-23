import pyttsx3

l = pyttsx3.init()
voices=l.getProperty('voices')
print("Available voice")
for index,voice in enumerate(voices):
    print(f"{index}:{voice.name}")

l.setProperty('reta',150)
choice = int(input("select a voice (number) : "))
l.setProperty('voice',voices[choice].id)

text=input("enter the text : ")
l.say(text)
l.runAndWait()