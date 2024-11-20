import cv2


image = cv2.imread('\Projact\\images\\\luux.jpg')
new = cv2.resize(image,(500,700))
cv2.imshow('hi',new)
cv2.imwrite('\Projact\\images\\\luux.jpg',new)
cv2.waitKey(0)