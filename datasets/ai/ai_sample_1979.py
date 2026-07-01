import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize our data
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

# Reshape image data
x_train = x_train.reshape((x_train.shape[0], 28, 28, 1))
x_test = x_test.reshape((x_test.shape[0], 28, 28, 1))

# Convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

# Create our neural network
model = keras.Sequential([
 keras.layers.Conv2D(32, 
  kernel_size=(3, 3),
  activation='relu',
  input_shape=(28, 28, 1)
 ),
 keras.layers.MaxPooling2D(pool_size=(2, 2)),
 keras.layers.Conv2D(64,
  kernel_size=(3, 3),
  activation='relu'
 ),
 keras.layers.MaxPooling2D(pool_size=(2, 2)),
 keras.layers.Flatten(),
 keras.layers.Dense(128, activation='relu'),
 keras.layers.Dense(10, activation='softmax')
])
model.compile(
 optimizer='adam',
 loss=keras.losses.categorical_crossentropy,
 metrics=['accuracy']
)

# Fit our model
model.fit(x_train, y_train, batch_size=64, epochs=2, verbose=1)

# Evaluate our model
score = model.evaluate(x_test, y_test, verbose=0)

# Print our model's accuracy
print('Test loss:', score[0])
print('Test accuracy:', score[1])