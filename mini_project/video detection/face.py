import cv2

#loading haarcascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


#loading video
cap = cv2.VideoCapture('test.mp4')
print ("press escape key to exit")

while True:
    _,img = cap.read()
    #it only works in grayscale.So we have to convert it into grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('img',img)
    k=cv2.waitKey(30) & 0xff
    if k == 27:
        break;
cap.release()
