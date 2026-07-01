import numpy as np
import tensorflow as tf
from tensorflow import keras

# Input Feature Vector
X = np.array([[2.7, 3735, 0.99, 8, 4000000]])

# Build model
model = keras.Sequential()
model.add(keras.layers.Dense(64, input_dim=X.shape[1], activation='relu'))
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(64, activation='relu'))
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(1, activation='sigmoid'))

# Compile Model
model.compile(loss='mean_squared_error', optimizer='adam')

# Fit the model
model.fit(X, y, epochs=50, batch_size=10, shuffle=True)