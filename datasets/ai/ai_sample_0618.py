import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense

# Create a Sequential model
model = Sequential()

# Add a hidden layer
model.add(Dense(20, input_dim=8, kernel_initializer='uniform', activation='relu'))

# Add an output layer
model.add(Dense(3, kernel_initializer='uniform', activation='softmax'))

# Compile the model
model.compile(optimizer=keras.optimizers.Adam(), loss=keras.losses.categorical_crossentropy, metrics=['acc'])

# Fit the model
model.fit(X_train, y_train, batch_size=64, epochs=10, validation_data=(X_test, y_test))