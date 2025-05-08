import cv2
import pyttsx3

voice = pyttsx3.init()

text = "Hy fire is here"

voice.setProperty('reta',150)

voice.setProperty('voice',voice.getProperty('voices')[0].id)

fire_cascade=cv2.CascadeClassifier(r'C:\PYTHON\OpenCv\PROJACT\cascades\fire.xml')

cam=cv2.VideoCapture(0)

while True :
    rat , frame = cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(frame,1.2,1)
    for (x,y,h,w) in fire:
        f1=gray[y:y+h, x:x+w]
        f2=frame[y:y+h, x:x+w]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        print("fire is here")
        voice.say(text)
        voice.runAndWait()
    cv2.imshow('moughit',frame)
    if cv2.waitKey(1) & 0xff == ord('a'):
        break