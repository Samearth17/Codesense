import pandas as pd 
import numpy as np 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Read the data 
df = pd.read_csv("Historical_Data.csv") 

# Select features 
X = df.iloc[:, 1:-1].values

# Target variable
y = df.iloc[:,-1].values

# Split into train & test sets 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Train the model 
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Make predictions
y_pred = regressor.predict(X_test)