import cv2

""" kifach ta3rad photo """ 

image = cv2.imread('img.jpg')
cv2.imshow('Moughit',image)

""" kifax t3raf lpcslat dyalt photo """
pix = image.size
f = image.shape
print("Number of pixels : ",pix)
print("dimensions : ", f)

""" tbdiil l7ajm dyal photo and fonitre """
new_image=cv2.resize(image,(400 ,200))
cv2.imshow('moughit',new_image)

""" kifax tbadl lcolor in photos"""
gray = cv2.cvtColor(new_image , cv2.COLOR_BGR2GRAY)
cv2.imshow('moughit',gray)

""" how to open photo and show photo and make s for save the photo and q for quit it  """


cv2.waitKey(0)