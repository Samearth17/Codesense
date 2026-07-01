# imports
import tensorflow as tf
from tensorflow import keras

# load the MNIST dataset
mnist = keras.datasets.mnist
# Split the dataset into training and testing sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# Preprocess the data
x_train, x_test = x_train / 255.0, x_test / 255.0

# create a model
model = keras.Sequential()
# add a convolution layer
model.add(keras.layers.Conv2D(28, kernel_size=(3,3), input_shape=(28, 28, 1)))
# add a max pooling layer
model.add(keras.layers.MaxPool2D(pool_size=(2, 2)))
# add a flatten layer
model.add(keras.layers.Flatten())
# add a dense layer
model.add(keras.layers.Dense(128, activation='relu'))
# add an output layer
model.add(keras.layers.Dense(10, activation='softmax'))

# compile the model
model.compile(optimizer='adam', 
 loss='sparse_categorical_crossentropy',
 metrics=['accuracy'])

# train the model
model.fit(x_train, y_train, epochs=5)

# evaluate the model
model.evaluate(x_test, y_test)