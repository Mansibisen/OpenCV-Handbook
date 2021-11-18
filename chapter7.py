import cv2
import numpy as np
def func(arg):
    pass

## detecting red color from the image

cv2.namedWindow("trackbar" )
cv2.resizeWindow("trackbar" , 640 , 240 )
cv2.createTrackbar("Hue Min" , "trackbar" , 0 , 179, func)
cv2.createTrackbar("Hue Max" , "trackbar" , 0 , 179, func)
cv2.createTrackbar("Sat Min" , "trackbar" , 0 , 255, func)
cv2.createTrackbar("Sat Max" , "trackbar" , 0 , 255, func)
cv2.createTrackbar("Val Min" , "trackbar" , 0 , 255, func)
cv2.createTrackbar("Val Max" , "trackbar" , 0 , 255, func)

while True:
    img = cv2.imread('Data/apple.jpg')
    imghsv = cv2.cvtColor(img , cv2.COLOR_BGR2HSV )
    hue_min = cv2.getTrackbarPos("Hue Min" , "trackbar")
    hue_max = cv2.getTrackbarPos("Hue Max", "trackbar")
    sat_min = cv2.getTrackbarPos("Sat Min", "trackbar")
    sat_max = cv2.getTrackbarPos("Sat Max", "trackbar")
    val_min = cv2.getTrackbarPos("Val Min", "trackbar")
    val_max = cv2.getTrackbarPos("Val Max", "trackbar")

    print(hue_min , hue_max , sat_min , sat_max , val_min , val_max)
    lower = np.array([hue_min , sat_min , val_min])
    upper = np.array([hue_max  ,sat_max , val_max])
    mask = cv2.inRange(imghsv , lower , upper)
    imgres = cv2.bitwise_and(img , img , mask = mask)
    cv2.imshow('output', img)
    cv2.imshow('output2', imghsv)
    cv2.imshow('output3' , mask)
    cv2.imshow('output4', imgres)
    cv2.waitKey(1)











