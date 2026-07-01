import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Start by loading in the data
data = pd.read_csv('sales_data.csv')

# Extract the inputs and the targets
inputs = data[['date', 'time', 'price', 'category', 'discount']]
targets = data.sales

# Create the model and train it
model = LinearRegression()
model.fit(inputs, targets)

# Make predictions
predictions = model.predict(inputs)