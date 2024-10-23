import cv2

cam = cv2.VideoCapture(0)
while True:
    rat , fram = cam.read()
    new=cv2.cvtColor(fram,cv2.COLOR_BGR2GRAY)
    cv2.imshow('moughit',new)
    if cv2.waitKey(1) & 0xff == ord('a'):
        break