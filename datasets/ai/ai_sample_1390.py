# Import necessary libraries
import numpy as np
from sklearn import tree

# Create the two classes
class_1 = [1, 0]
class_2 = [0, 1]

# Initialize the dataset of features
data_set = np.array([ 
    [172, 80, 10, 28, 0],
    [188, 78, 11, 33, 0],
    [150, 55, 8, 21, 1],
    [170, 68, 9, 22, 1],    
])

# Initialize the labels
labels = np.array([class_1, class_2, class_2, class_1])

# Create the decision tree classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(data_set, labels)

# Create a prediction
prediction = clf.predict([[187,77,11,34,0]])

# Output the prediction
if prediction == class_1: 
    print("Prediction: Class 1")
elif prediction == class_2:
    print("Prediction: Class 2")