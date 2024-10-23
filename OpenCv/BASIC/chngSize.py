import cv2

image = cv2.imread('C:\Users\ABDELMOUGHIT\Bureau\pythonprojacts')
new_size = cv2.resize(image,(300,300))
cv2.imshow('moughit',new_size)

cv2.waitKey(0)