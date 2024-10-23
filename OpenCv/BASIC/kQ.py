import cv2 

image = cv2.imread('Designs\img.jpg')
cv2.line(image,(15,15),(1000,20),(1,345,1),4)
cv2.rectangle(image,(15,15),(750,100),(0,255,0),4)
cv2.imshow('moughit',image)
k=cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('C:\\img.png')
    cv2.destroyAllWindows()