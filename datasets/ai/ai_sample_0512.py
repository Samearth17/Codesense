import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Read in the stock data
data = pd.read_csv('aapl_stock_data.csv')

# Create the features and labels datasets
X = data[['High', 'Low', 'Close', 'Volume']]
y = data['Adj Close']

# Create a linear regression model
reg = LinearRegression().fit(X, y)

# Make predictions
predictions = reg.predict(X)

# Calculate the error between predictions and actual values
error = np.mean(np.abs((y - predictions) / y) * 100)

# Print out the results
print('Mean Absolute Percent Error: {:.2f}%'.format(error))