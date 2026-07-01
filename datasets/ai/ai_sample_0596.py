#Import necessary libraries
import cv2
import numpy as np

#Load the classifier for frontal face detection
haar_face_cascade = cv2.CascadeClassifier("haarcascade_frontal_face.xml")

#Create a VideoCapture object
capture = cv2.VideoCapture("Sample_image.jpg")
img = capture.read()

#Convert the image into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detect facial features
faces = haar_face_cascade.detectMultiScale(gray, 1.3, 5)

#Draw a rectangle around the faces
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

#Write the image into a file
cv2.imwrite('face_detect.jpg',img)