# Load the necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Read in the data
train_data = pd.read_csv("data.csv")

# Split the data into X (predictors) and y (response)
X = train_data.drop('response', axis=1)
y = train_data['response']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Define the model and fit it
model = ...
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Score the prediction
score = accuracy_score(y_test, y_pred)

# Submit the prediction to Kaggle
# ...