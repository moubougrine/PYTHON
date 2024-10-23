import playsound
from gtts import gTTS

Say = input("Enter something : ")
sound=gTTS(text=Say)
sound.save('welcome.mp3')
playsound.playsound('welcome.mp3')