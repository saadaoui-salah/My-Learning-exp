import cv2

face_cascade = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")
cdef int img = cv2.imread('Snapchat-1493665167.jpg')

cdef int GrayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cdef int faces = face_cascade.detectMultiScale(GrayImg, 1.1 ,4)
cdef int y
cdef int x
cdef int w
cdef int h
for (x, y, w, h) in faces:

    cv2.rectangle(img, (x, y),(x+w, y+h),(255,0,0),4) 
    cv2.putText(img,"face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

cv2.imshow('img',img)

cv2.waitKey()
