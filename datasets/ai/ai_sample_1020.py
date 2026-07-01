import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM

def create_model(input_shape):
    model = Sequential()
    model.add(LSTM(128, input_shape=input_shape))
    model.add(Dropout(0.3))
    model.add(Dense(1))
    model.compile(loss='mse', optimizer='rmsprop')
    return model

input_shape = (X_train.shape[1],1)
model = create_model(input_shape)
model.fit(X_train, y_train, batch_size=32, epochs=30)