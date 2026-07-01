"""
Predicts the stock price of a given company in the next 30 days
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

#Get the historical stock prices
data = pd.read_csv('historical_stock_prices.csv')

#Train the linear regression model using the historical stock prices
X = data['date'].values.reshape(-1,1)
y = data['price'].values.reshape(-1,1)
linear_regressor = LinearRegression()  
linear_regressor.fit(X, y)

#Predict the stock prices for the next 30 days
next_30_days = np.arange(X.flatten()[-1]+1, X.flatten()[-1]+30, 1).reshape(-1,1)
y_pred = linear_regressor.predict(next_30_days)

#Print the predicted stock prices
print("The predicted stock prices for the next 30 days are:")
for i in range(30):
  print("Date:", next_30_days[i][0],"Price:",y_pred[i][0])