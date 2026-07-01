#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#import data
data = pd.read_csv('data.csv') 

#split data into train and test data
X_train=data.iloc[:, 0] #Choosing the independent variable 
y_train=data.iloc[:, 1]  #Choosing the dependent variable
X_test=data.iloc[:, 0] #Choosing the independent variable 
y_test=data.iloc[:, 1]  #Choosing the dependent variable

#Build a deep learning model
#import necessary libraries
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential

#create a model and add layers
model = Sequential()
model.add(Dense(64, input_shape=(1,), activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(1))

#compile the model
model.compile(optimizer='adam', loss='mse', metrics=['mse'])

#train the model
model.fit(X_train, y_train, batch_size=64, epochs=20, validation_data=(X_test, y_test))

#Evaluate the model
score = model.evaluate(X_test, y_test, verbose=0)