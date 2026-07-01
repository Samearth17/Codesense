"""
Develop a neural network model in Python to recognize a hand-written number
"""

import numpy as np
import tensorflow as tf

#load the mnist dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

#discretize the images by flattening them
x_train = x_train.reshape(-1, 784) 
x_test = x_test.reshape(-1, 784)

#normalize the pixel values from 0 to 1
x_train = x_train/255.0
x_test = x_test/255.0

#create a neural network model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(512, activation='relu', input_shape= (784,)))
model.add(tf.keras.layers.Dense(512, activation='relu'))
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.Dense(10, activation='softmax'))

#compile and train the model
model.compile(
    loss='sparse_categorical_crossentropy', metrics=['accuracy']
)
model.fit(x_train, y_train,  epochs = 10)

#evaluate the model
model.evaluate(x_test, y_test)