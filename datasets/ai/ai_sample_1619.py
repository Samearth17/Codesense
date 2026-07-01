"""
Construct a neural network in Python to predict the price of Bitcoin for the next 5 days
"""

import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler

# Load the dataset
dataset = pd.read_csv('BTC-USD.csv')

# Get the values
closing_prices = dataset.iloc[:, [4]].values

# Normalize the data
scaler = MinMaxScaler(feature_range=(0, 1))
prices_scaled = scaler.fit_transform(closing_prices)

# Create the input data for the model
X, Y = [], []
for i in range(30, len(prices_scaled)):
    X.append(prices_scaled[i-30:i, 0])
    Y.append(prices_scaled[i, 0])
X, Y = np.array(X), np.array(Y)

# Reshape the input
X = np.reshape(X, (X.shape[0], X.shape[1], 1))

# Create the model
model = Sequential()
model.add(LSTM(128, input_shape=(X.shape[1], 1)))
model.add(Dense(1))
model.compile(loss='mse', optimizer='adam')

# Train the model
model.fit(X, Y, epochs=100, batch_size=32)

# Prepare the 5-day prediction data
prediction_data = prices_scaled[-30:, 0]
prediction_data = np.reshape(prediction_data, (1, 30, 1))

# Make the 5-day prediction
predictions = model.predict(prediction_data)
prediction = scaler.inverse_transform(predictions)
print(prediction)