import numpy as np
import matplotlib.pyplot as plt


class LinearRegression:
 def __init__(self):
 self.weights = None
 self.bias = None

 def fit(self, X, y):
"""
Fit the linear regression model to the given data

Parameters
----------
X : array-like, shape (n_samples, n_features)
Training data

y : array-like, shape (n_samples,)
Target values

Returns
-------
self : returns an instance of self.
"""
 
 # Compute the weights and bias
 X = np.array(X)
 y = np.array(y)
 weights = np.dot(np.linalg.pinv(X), y)
 bias = y - np.dot(X, weights)
 
 self.weights = weights
 self.bias = bias
 
 def predict(self, x):
"""
Predict the output value for a given input

Parameters
----------
x : array-like, shape (n_samples, n_features)
Input data

Returns
-------
y : array-like, shape (n_samples,)
Predicted output value
"""
 
 # Return the predictions using the weights and bias
 predictions = np.dot(np.array(x), self.weights) + self.bias
 return predictions