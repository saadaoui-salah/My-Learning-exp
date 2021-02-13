import cv2

face_cascade = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")

img = cv2.imread('Snapchat-1493665167.jpg')

GrayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(GrayImg, 1.1 ,4)

for (x, y, w, h) in faces:

    cv2.rectangle(img, (x, y),(x+w, y+h),(255,0,0),4) 
    cv2.putText(img,"face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
cv2.imshow('img',img)

cv2.waitKey()

#cam = cv2.VideoCapture(2)
#if not (cam.isOpened()):
#    print("couldn't")
#cam.set(3, 640)
#cam.set(4, 480)
#cam.set(10,150)
#while True:
#    suc, img = cam.read()
#    print(suc)
#    cv2.imshow("camera", img)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break