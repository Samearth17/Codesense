import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC

# Load data
X = np.array([[1,2,3], [-1,2,5], [-1,2,7], [5,5,5], [3,3,3], [5,5,7]])
y = np.array([0, 0, 0, 1, 0, 1])

# Initialize classifier
clf = SVC(kernel='linear')

# Fit data
clf.fit(X, y)

# Test classifier
x_test = np.array([[2,2,2], [4,4,4]])

prediction = clf.predict(x_test)
print(prediction)