# Import libraries necessary for building the neural network 
import numpy as np 
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# Read in the dataset
dataset = pd.read_csv('dataset.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

# Building the neural network
model = Sequential()

# First layer with input dimensions
model.add(Dense(32, activation='relu', input_dim=X.shape[1]))
model.add(Dropout(0.2))

# Second layer
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.2))

# Output layer
model.add(Dense(1, activation='sigmoid'))

# Compile the model 
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Fit the model
model.fit(X, y, epochs=100, batch_size=32, validation_split=.2)