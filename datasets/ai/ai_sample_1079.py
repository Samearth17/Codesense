"""
Perform linear regression to predict the sales for a new product
"""

import numpy as np
from sklearn.linear_model import LinearRegression

# Define input values
product_price = 90
advertisement_budget = 15

# Define the independent and dependent data
X = np.array([advertisement_budget]).reshape(-1,1)
Y = np.array([product_price]).reshape(-1,1)

# Create and train the model
linear_regressor = LinearRegression()
linear_regressor.fit(X, Y)

# Make a prediction
predicted_sales = linear_regressor.predict([[advertisement_budget]])

# Print the result
print("Predicted sales for new product: ", predicted_sales[0])