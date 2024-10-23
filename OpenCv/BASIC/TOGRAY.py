import cv2

image = cv2.imread('img.jpg')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('moughit',gray)
cv2.waitKey(0)