import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression

# Loading the data
data = pd.read_csv('housing.csv')

# Feature selection & Data Splitting
X = data[['square_feet', ' bedrooms', 'bathrooms', 'location']]
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create the model & Training
model = LinearRegression()
model.fit(X_train, y_train)

# Testing & Evaluating
y_pred = model.predict(X_test)

# Visualizing the results
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.show()