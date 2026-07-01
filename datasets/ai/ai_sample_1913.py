"""
Create a neural network in Python to recognize the handwritten digits from 0 to 9.
"""

import tensorflow as tf
import numpy as np
from tensorflow import keras

# load the MNIST dataset
mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# normalize the data
x_train, x_test = x_train/255.0, x_test/255.0

# build the model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(256, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

# compile and fit the model
model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=10)

# evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print("Test accuracy: ", test_acc)