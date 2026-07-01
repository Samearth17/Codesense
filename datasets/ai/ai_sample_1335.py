import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv('people.csv') 

# Split the features and labels
X = data[['Name']]
y = data['Age'].values

# Create and train the model
model = LinearRegression().fit(X, y)

# Make predictions with the model
predictions = model.predict(X)
print(predictions)