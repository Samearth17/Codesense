import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('seattle_house_prices.csv')

# Select feature and target columns
X = data.iloc[:,:-1]
y = data.iloc[:,-1]

# Split data into training and test sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the model
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()  
regressor.fit(X_train, y_train) 

# Make predictions on the test data
y_pred = regressor.predict(X_test)

# Evaluate the model
from sklearn.metrics import r2_score

r2_score(y_test, y_pred)