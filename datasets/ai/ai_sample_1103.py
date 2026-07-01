# Import the necessary libraries
import matplotlib.pyplot as plt
from keras.datasets import mnist 
from keras.models import Sequential
from keras.layers import Dense 

# Load the datasets
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Reshape the input
X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)

# Build a fully-connected neural network 
model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=784))
model.add(Dense(units=10, activation='softmax'))

# Compile the model 
model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, batch_size=32, epochs=3, verbose=1)

# Test the model by evaluating on the test data 
score = model.evaluate(X_test, y_test, verbose=1)

# Summary 
print("Test accuracy: ", score[1])