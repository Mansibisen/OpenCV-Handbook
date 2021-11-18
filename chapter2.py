import cv2
import numpy as np
## processing the images
img = cv2.imread("Data/lena.jpg")
imgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY) ## used to convert the images in specific scales we wants
cv2.imshow("output" , imgGray)
cv2.waitKey(0)

## function to blurr
imgblurr = cv2.GaussianBlur(img , (7 , 7) , 0) ## digits in bracket are kernel size and they will be only odd numbers
cv2.imshow("output2" , imgblurr)
cv2.waitKey(0)
## edge detection
imgCaned = cv2.Canny(img , 150 , 150) ## parameters are about complexity of edges you want
cv2.imshow("output3" , imgCaned)
cv2.waitKey(0)
## dialation
imgdial = cv2.dilate(imgCaned , np.ones((5,5) , np.uint8 ), iterations = 1 ) ## parameters are about kernel
cv2.imshow("output4" , imgdial)
cv2.waitKey(0)
## errosion
imgerros = cv2.erode(imgdial , np.ones((5,5) , np.uint8 ), iterations = 1 ) ## parameters are about kernel
cv2.imshow("output5" , imgerros)
cv2.waitKey(0)