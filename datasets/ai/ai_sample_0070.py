import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
 
# Load the data
data = pd.read_csv('data.csv')
 
# Split the data into features and labels
X = data.drop(['label'], axis=1).values
y = data['label'].values
 
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
 
# Create the neural network
model = Sequential()
model.add(Dense(12, input_dim=X.shape[1], kernel_initializer='normal', activation='relu'))
model.add(Dense(12, kernel_initializer='normal', activation='relu'))
model.add(Dense(1, kernel_initializer='normal'))
 
# Compile the model
model.compile(loss='mean_squared_error', optimizer='adam')
 
# Train the model
model.fit(X_train, y_train, epochs=100, batch_size=20, verbose=0)
 
# Evaluate the model
score = model.evaluate(X_test, y_test, verbose=0)
print('Test score:', score)