# Load MNIST dataset
import pandas as pd
dataset = pd.read_csv("MNIST.csv")

# Divide the dataset into inputs and labels
X = dataset.iloc[:, 1:784].values 
y = dataset.iloc[:, 0].values

# Reshape the dataset
X = X.reshape(len(X), 28, 28, 1)

# Preprocessing
X = X / 255.0

# Create the neural network
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# Initialize the CNN
classifier = Sequential()

# Convolution Layer
classifier.add(Convolution2D(32, 3, 3, input_shape = (28, 28, 1), activation = 'relu'))

# Pooling
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Flattening
classifier.add(Flatten())

# Fully Connected Layer
classifier.add(Dense(output_dim = 128, activation = 'relu'))
classifier.add(Dense(output_dim = 10, activation = 'sigmoid'))

# Compiling the CNN
classifier.compile(optimizer='adam',loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Fit CNN to the training set
classifier.fit(X, y, batch_size=32, epochs=3, verbose=1)