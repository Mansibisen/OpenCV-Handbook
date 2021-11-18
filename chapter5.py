import cv2
import numpy as np

## to get bird eye view (flattening the image)
img = cv2.imread('Data/lena.jpg')
width = 250
height = 350
points = np.float32([[111  , 150 ], [ 145 , 200] ,[ 450 , 560]  , [490 , 600] ] )
points2 = np.float32([[0, 0], [width , 0] ,[0 , height ]  , [width , height] ] )
matrix  = cv2.getPerspectiveTransform(points , points2)
imgout = cv2.warpPerspective(img , matrix , (width , height))




cv2.imshow('output', img)
cv2.imshow('output2', imgout)
cv2.waitKey(0)












