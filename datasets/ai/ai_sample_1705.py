import cv2

# load the cascade classifier
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Read the input image
img = cv2.imread("input.jpg")

# Convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect the faces
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)
# Draw the rectangle around each face
for x, y, w, h in faces:
 cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

# Detect the facial expressions
gray_faces = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
for x, y, w, h in faces:
 face_img = gray_faces[y:y + h, x:x + w]
 expression = expression_model.predict(face_img)
 
# Output
print("The expression of the person is: {}".format(expression))