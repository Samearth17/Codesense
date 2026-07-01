import numpy as np

# Define the data points
points = np.array([[1, 5], [2, 3], [3, 4]])

# Define the labels
labels = np.array([1, -1, -1])

# Define the parameters of the algorithm
b = 0
w0 = 0
w1 = 0
learning_rate = 0.001

# Define the training loop
for i in range(100):
 pred = w0 + w1 * points[:, 0] > b
 loss = np.mean((labels - pred) ** 2)
 dloss_dw0 = 2 * np.mean(points[:, 0] * (labels - pred))
 dloss_dw1 = 2 * np.mean(points[:, 1] * (labels - pred))
 dloss_db = 2 * np.mean(labels - pred)
 
 # update parameters
 w0 = w0 + learning_rate * dloss_dw0
 w1 = w1 + learning_rate * dloss_dw1
 b = b + learning_rate * dloss_db

# Define the prediction function
def predict(x):
 pred = w0 + w1 * x > b
 
 if pred:
 return "Positive"
 else:
 return "Negative"