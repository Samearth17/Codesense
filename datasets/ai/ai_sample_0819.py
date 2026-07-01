# import the necessary libraries
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split

# Read the dataset
data = pd.read_csv('dataset.csv')

# Split the dataset into train and test datasets
x_train, x_test, y_train, y_test = train_test_split(data.iloc[:,:-1], data.iloc[:,-1], test_size=0.2)

# Create the isolation forest model
model = IsolationForest()
model = model.fit(x_train, y_train)

# Make predictions
y_pred = model.predict(x_test)

# Evaluate the model performance
from sklearn.metrics import accuracy_score
print('Accuracy:', accuracy_score(y_test, y_pred))