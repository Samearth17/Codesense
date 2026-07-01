import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

# Read data from CSV
data = pd.read_csv('data.csv')

# Set X and Y
X = data['X']
Y = data['Y']

# Create linear regression model
model = linear_model.LinearRegression()

# Train the model
model.fit(X, Y)

# Make predictions
Y_pred = model.predict(X)

# Visualize the results
plt.scatter(X, Y)
plt.plot(X, Y_pred, color='red')
plt.show()