import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM

# Load the data
df = pd.read_csv('FB.csv')
df.head()

# Preprocess the data
data = df.filter(['Close'])
dataset = data.values
scaler = MinMaxScaler()
dataset = scaler.fit_transform(dataset)

# Create the model
model = Sequential()
model.add(LSTM(50, return_sequences = True, input_shape = (dataset.shape[1], 1)))
model.add(LSTM(50, return_sequences = False))
model.add(Dense(25))
model.add(Dense(1))

# Train the model
model.compile(optimizer = 'adam', loss = 'mean_squared_error')
model.fit(dataset, batch_size = 1, epochs = 10)