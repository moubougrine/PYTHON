import cv2

video=cv2.VideoCapture('Designs\pytvid.mp4')
while True:
    rate , fram = video.read()
    cv2.imshow('moughit',fram) 
    if cv2.waitKey(1) & 0xff == ord('a'):
        break