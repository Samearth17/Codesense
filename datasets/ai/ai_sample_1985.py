# Load required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load the dataset
data = pd.read_csv("dataset.csv")

# Extract features and target variable
X = data.drop('output',axis=1)
y = data.output

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42).fit(X_train, y_train)

# Get predictions
y_pred = model.predict(X_test)

# Evaluate the model
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test,y_pred)

# Return results
return mse