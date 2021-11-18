## drawing shapes lines and text
import cv2
import numpy as np
black = np.zeros((512,512 , 3) , np.uint8)

#black[:] =  255 , 0  , 0   ## changing the color
cv2.line(black , (0, 0) , (300 , 300) , (0 , 255 , 0))
cv2.rectangle(black , (0, 0) , (400 , 400) , (255 , 0 , 0) , cv2.FILLED)
cv2.circle(black , (250 , 250) , 30 , (0 , 0 , 255) , 3)
cv2.putText(black ,"mansi",(300 , 300) , cv2.FONT_HERSHEY_COMPLEX , 2, (129 , 45 ,188))




cv2.imshow("output", black)
cv2.waitKey(0)