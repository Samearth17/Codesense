import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Read in csv data
data = pd.read_csv('stock_data.csv')

# Split our data into testing and training sets
X_train = data[data['date'] < '2014-01-01']
X_test = data[data['date'] >= '2014-01-01']

# Extract our feature and target columns
X_train = X_train.drop(['date', 'price'], axis=1)
X_test = X_test.drop(['date', 'price'], axis=1)
y_train = data[data['date'] < '2014-01-01']['price']
y_test = data[data['date'] >= '2014-01-01']['price']

# Fit our Linear Regression Model
linear_regression = LinearRegression()
linear_regression.fit(X_train, y_train)
y_preds = linear_regression.predict(X_test)

# Print out our predictions
for i in range(1, len(y_preds)):
 print(f"Predicted: {y_preds[i]}, Actual: {y_test.iloc[i]}")