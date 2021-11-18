import cv2
import numpy as np

## resizing the image
img = cv2.imread('Data/lena.jpg')
print(img.shape)
imgResize = cv2.resize(img ,(300 , 200))
print(imgResize.shape)
cv2.imshow('output', imgResize)
cv2.waitKey(0)

## croping the image


imgCropped = img[0:200, 200:500]

cv2.imshow('output2', imgCropped)
cv2.waitKey(0)