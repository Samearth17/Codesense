import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the dataset
dataset = pd.read_csv('AAPL.csv')

# Separate the dataset into features and labels
#labels = dataset['Label']
y = np.array(dataset['Close'])
dataset.drop("Close", axis=1, inplace=True)
x = np.array(dataset)

# Split the data into training and testing sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

# Create the model
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=100)

# Train the model
regressor.fit(x_train, y_train)

# Make predictions
y_pred = regressor.predict(x_test)

# Check the accuracy
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, y_pred)
print("Mean squared error:", mse)