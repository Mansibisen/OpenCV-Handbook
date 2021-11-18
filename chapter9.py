import cv2
import numpy as np


## face detection using cascade
img = cv2.imread('Data/lena.jpg')
cascade = cv2.CascadeClassifier(path)
imggray = cv2.cvtColor( img , cv2.COLOR_BGR2GRAY)
obj_Detected = cascade.detectMultiScale(imggray , 1.1 , 4)
for( x , y, w , h) in obj_Detected:
    cv2.rectangle(img , (x,y) , (x +w , y+h) , (255 , 0 , 0) , 2)



cv2.imshow('output', img)

cv2.waitKey(0)
