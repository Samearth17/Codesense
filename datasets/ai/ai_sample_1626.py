# import the necessary packages
from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dense

# Construct the model 
model = Sequential()
model.add(Conv2D(20, (5, 5), padding="same",
input_shape=(28, 28, 1)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Flatten())
model.add(Dense(units=500))                 # Number of nodes in the hidden layer
model.add(Activation("relu"))
model.add(Dense(units=10))                  # Output layer with 10 classes
model.add(Activation("softmax"))

# Compile the model
model.compile(loss="categorical_crossentropy",
   optimizer="adam", metrics=["accuracy"])