import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Read data
data = pd.read_csv("xyz.csv")

# Separate data for prediction
X = np.array(data['Date']).reshape(-1, 1) 
y = np.array(data['Price']).reshape(-1, 1)

# Train the model
model = LinearRegression()
model.fit(X, y)

# Predict the prices
predicted_price = model.predict(np.array(["2020-10-01"]).reshape(-1, 1))
print("Predicted Stock Price for 2020-10-01:", predicted_price[0][0])