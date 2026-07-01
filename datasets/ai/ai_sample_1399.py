from sklearn.linear_model import LinearRegression
import numpy as np

# Load the data
X = np.array([[1000], [2000], [3000]])
y = np.array([20000, 40000, 60000])

# Create the linear regression model
model = LinearRegression()

# Train the model with the data
model.fit(X, y)

# Print the model parameters
print('Intercept:', model.intercept_) 
print('Coefficient:', model.coef_)