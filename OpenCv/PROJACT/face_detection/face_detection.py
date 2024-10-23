import cv2

camer = cv2.VideoCapture(0)
face = cv2.CascadeClassifier('cascades\\haarcascade_frontalface_default.xml')

while True :
    rate, frame = camer.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    f = face.detectMultiScale(gray,1.2,20)
    for (x,y,h,w) in f :
        cv2.rectangle(frame,(x,y),(x+w, y+h),(0,255,0),5)
    cv2.imshow('Moughit',frame)
    if cv2.waitKey(1) & 0xff == ord('a'):
        break

camer.release()
cv2.destroyAllWindows()
