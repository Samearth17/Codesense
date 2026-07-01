from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
import numpy as np

# define constants
time_steps = 60
batch_size = 32

# build the model
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(time_steps, 1)))
model.add(Dropout(0.2))

model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(units=50))
model.add(Dropout(0.2))

model.add(Dense(units=1))

model.compile(optimizer='adam', loss='mean_squared_error')

# read the data 
dataset = np.loadtxt('data.csv', delimiter=',')

data = dataset[:, 0:1]

# create train and test data
x_train = data[:int(len(data)*0.8)]
x_test = data[int(len(data)*0.8):]

# reshape the data for input format
x_train = np.reshape(x_train, (x_train.shape[0], time_steps, 1))
x_test = np.reshape(x_test, (x_test.shape[0], time_steps, 1))

# train the model
model.fit(x_train, x_train, epochs=50, batch_size=batch_size, validation_data=(x_test, x_test))