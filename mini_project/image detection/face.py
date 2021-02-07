import cv2

#loading haarcascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


#loading images
img = cv2.imread('test.jpg')
img = cv2.resize(img,(960,540))

#it only works in grayscale.So we have to convert it into grayscale

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.1,4)

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('img',img)
print ("press any key to exit")  
cv2.waitKey()
