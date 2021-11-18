import cv2
#print('imported')
# how to read images , videos , webcams

#img = cv2.imread('Data/lena.jpg')

#cv2.imshow('output', img)
#cv2.waitKey(0)
#video = cv2.VideoCapture("Data/samplevideo.mp4")
'''while True:
    success , video_to_img = video.read()
    cv2.imshow('video', video_to_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;
'''
## using a webcam
webCam = cv2.VideoCapture(0)
webCam.set(3 , 600)
webCam.set(4 , 500)
webCam.set(10 , 100) ## brightness 10 is ID
while True:
    success , cam_to_img = webCam.read()
    cv2.imshow('video', cam_to_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;
