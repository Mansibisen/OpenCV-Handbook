import cv2
import numpy as np
## joining images together
img = cv2.imread('Data/lena.jpg')

hor = np.hstack((img , img))
cv2.imshow('output', hor)
ver = np.vstack((img , img))
cv2.imshow('output2', ver)
cv2.waitKey(0)