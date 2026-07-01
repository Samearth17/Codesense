"""
Perform stochastic gradient descent on the iris dataset in Python.
"""

import numpy as np
from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split

# Load the dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Split the dataset into test and train sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Set the hyperparameters
NUM_ITERATIONS = 1000 
LEARNING_RATE = 0.01

# Initialize the weights
w = np.zeros(X_train.shape[1])
b = np.zeros((1,)) 

# Perform the Stochastic Gradient Descent
for n in range(NUM_ITERATIONS):
    # Pick a random point
    x_i, y_i = X_train[np.random.randint(X_train.shape[0])], y_train[np.random.randint(y_train.shape[0])]

    # Compute the Sigmoid
    z = np.matmul(w, x_i) + b 
    sigmoid = 1 / (1 + np.exp(-z))

    # Compute the Gradients
    dw = (sigmoid - y_i) * x_i
    db = (sigmoid - y_i) 

    # Update the weights
    w = w - LEARNING_RATE * dw 
    b = b - LEARNING_RATE * db

# Make predictions
y_pred = np.matmul(X_test, w) + b
y_pred = np.round(1 / (1 + np.exp(-y_pred)))

# Compute the accuracy
accuracy = metrics.accuracy_score(y_test, y_pred) 
print("Accuracy:", accuracy)