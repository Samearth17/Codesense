import tensorflow as tf
from tensorflow import keras
import numpy as np

# define 2-D data points with four different classes 
x_train = np.array([[1,2], [2,4], [4,2], [2,1], [4,4], [3,3], [3,1], [1,3]])
y_train = np.array([0,0,1,1,2,2,3,3])

# define the network model
model = keras.Sequential([
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(4, activation='softmax')
])

# compile the model 
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# train the model
model.fit(x_train, y_train, epochs=10)