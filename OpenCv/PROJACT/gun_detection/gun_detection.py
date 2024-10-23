import cv2
import imutils

gun_cascade = cv2.CascadeClassifier('cascades\\cascade.xml')

camera = cv2.VideoCapture(0)

f1 = False
f2 = None

while True:
    ret, frame = camera.read()

    if not ret:
        print("Failed to capture frame")
        break
    
    frame = imutils.resize(frame, width=700)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    gun = gun_cascade.detectMultiScale(gray, 1.2, 15, minSize=(100, 100))
    
    f1 = len(gun) > 0
    
    for (x, y, w, h) in gun:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2) 
    
    if f2 is None:
        f2 = gray
        continue
    
    cv2.imshow('Gun Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

    if f1:
        print("The gun is detected")
    else:
        print("Guns didn't detect")

camera.release()
cv2.destroyAllWindows()
