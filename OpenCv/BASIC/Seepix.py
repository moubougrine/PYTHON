import cv2

image= cv2.imread('Designs\img.jpeg')
pix = image.size
dimension=image.shape
print("Number of pix : ",pix)
print("Number of dimensions : ",dimension)
