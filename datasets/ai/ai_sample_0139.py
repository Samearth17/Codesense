# Importing necessary libraries

import numpy as np
import pandas as pd
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Dense, Input, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.utils import to_categorical

# Loading data
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Defining the neural network model

# Input layer
inputs = Input(shape=(28,28,))

# Hidden layer
h1 = Dense(64, activation='relu')(inputs)
h2 = Dropout(0.5)(h1)

# Output layer
outputs = Dense(10, activation='softmax')(h2)

# Compiling the model
model = Model(inputs=inputs, outputs=outputs)
model.compile(loss='categorical_crossentropy',
 optimizer='adam',
 metrics=['accuracy'])

# Data pre-processing

# Reshape inputs from (60000, 28, 28) to (60000, 784)
X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)

# Normalize pixel values
X_train = X_train.astype('float32')
X_train /= 255
X_test = X_test.astype('float32')
X_test /= 255

# One-hot encode labels
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

# Fitting the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=5, batch_size=128)