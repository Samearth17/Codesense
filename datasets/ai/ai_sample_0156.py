# Import the necessary libraries 
from sklearn.datasets import fetch_openml
import numpy as np
from sklearn.linear_model import LogisticRegression

#Load the dataset
mnist = fetch_openml('mnist_784')

# Split into features and labels
X = mnist.data
y = mnist.target

# Reshape data to be valid
X = X.reshape((X.shape[0], -1))
print(X.shape, y.shape)

# Create a Logistic Regression classifier 
clf = LogisticRegression()

# Fit the model to the data 
clf.fit(X, y)