import random
import numpy as np

def sgd_model(X, Y, w, b, learning_rate, epochs):
    """Implement Stochastic Gradient Descent to generate a linear regression model"""
    N = len(X)

    for e in range(epochs):
        for i in range(N):

            x = X[i]
            y = Y[i]

            # Calculate output
            yhat = w * x + b

            # Update weights
            w += learning_rate * (y - yhat) * x
            b += learning_rate * (y - yhat)
    return w, b

# Example
X = np.array([1, 2, 3])
Y = np.array([1, 2, 3])
w, b = sgd_model(X, Y, 0, 0, 0.01, 1000)
yhat = w * X + b