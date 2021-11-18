import numpy as np
import cv2

## detecting shapes in the images

img = cv2.imread('Data/shapes.png')
imggray = cv2.cvtColor( img , cv2.COLOR_BGR2GRAY)
imgblurr = cv2.GaussianBlur(imggray , (7 , 7) , 1)
imgcanned = cv2.Canny( imgblurr , 50 , 50)
imgcontour = img.copy()
## finding the counters
def contours(img):
    contours, hierarchy = cv2.findContours(img , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
    for i in contours:
        area = cv2.contourArea(i)
        print(area)

        if area > 250:
            cv2.drawContours(imgcontour, i, -1, (255, 0, 0), 6)
            arc = cv2.arcLength(i , True)
            cornorapprox = cv2.approxPolyDP(i , 0.02*arc, True)
            objcornor = len(cornorapprox)
            x , y , w , h,  = cv2.boundingRect(cornorapprox)
            cv2.rectangle( imgcontour , (x , y), (x+w , y+h) , (0 , 255 , 255) , 2)

            if objcornor == 3 :
                objecttype = "Tri"
            elif objcornor == 4 :
                r= w/float(h)
                if( r > 0.95 and r < 0.01):
                    objecttype = "square"
                else:
                    objecttype = "rectangle"
            elif objcornor > 4:
                objecttype = "circle"

            else:
                objecttype = "none"

            cv2.putText(imgcontour , objecttype , (x+(w//2)-10 , y+(h//2)-10) , cv2.FONT_HERSHEY_COMPLEX   , 0.5 , (255 , 255 , 0) )
contours(imgcanned)
cv2.imshow('output', img)
cv2.imshow('output2', imggray)
cv2.imshow('output3', imgblurr)
cv2.imshow('output4', imgcanned)
cv2.imshow('output5', imgcontour)
cv2.waitKey(0)