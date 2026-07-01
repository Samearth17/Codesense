"""
Recognize handwritten digits using OpenCV library
"""
import cv2
import numpy as np

# Load the model
model = cv2.ml.SVM_load('svm_model.xml')

# Read the input image
img = cv2.imread('input.png')

# Convert to grayscale and apply Gaussian filtering
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray = cv2.GaussianBlur(img_gray, (5,5), 0)

# Threshold the image
ret, img_thresh = cv2.threshold(img_gray, 90, 255, cv2.THRESH_BINARY_INV)

# Find contours
_, ctrs, _ = cv2.findContours(img_thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Get rectangles contains each contour
rects = [cv2.boundingRect(ctr) for ctr in ctrs]

# For each rectangular region, calculate HOG features and predict
# the digit using Linear SVM.
for rect in rects:
    # Draw the rectangles
    #cv2.rectangle(img, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3) 
    # Make the rectangular region around the digit
    leng = int(rect[3] * 1.6)
    pt1 = int(rect[1] + rect[3] // 2 - leng // 2)
    pt2 = int(rect[0] + rect[2] // 2 - leng // 2)
    roi = img_thresh[pt1:pt1+leng, pt2:pt2+leng]
    # Resize the image
    roi = cv2.resize(roi, (64, 64), interpolation=cv2.INTER_AREA)
    roi = cv2.dilate(roi, (3, 3))
    # Calculate the HOG features
    roi_hog_fd = hog(roi, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(1, 1), visualize=False)
    roi_hog_fd = np.asarray(roi_hog_fd, dtype=np.float32)
    # Predict the digit using Linear SVM
    nbr = model.predict(roi_hog_fd)
    #cv2.putText(img, str(int(nbr[0][0])), (rect[0], rect[1]),cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 255), 3)
    print(int(nbr[0][0]))