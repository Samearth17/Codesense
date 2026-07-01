import numpy as np
from sklearn.linear_model import LinearRegression

# Create data
x = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
# Create target
y = np.dot(x, np.array([1, 2])) + 3

# Create a linear regression model
model = LinearRegression()
# Fit the model
model.fit(x, y)

# Make prediction
x_test = np.array([3, 5])
y_test = model.predict([x_test])

# Output prediction
print("Predicted value of y given x=[3,5] :", y_test[0])