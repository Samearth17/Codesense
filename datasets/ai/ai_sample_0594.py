import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Create the data
data = {'Monthly Income': [1900, 2300, 2800, 3500],
        'Monthly Expenses': [750, 850, 950, 1250]}
df = pd.DataFrame(data)

# Train the model
x = df['Monthly Income'].values.reshape(-1, 1)
y = df['Monthly Expenses'].values
reg = LinearRegression().fit(x, y)

# Create the prediction
prediction = reg.predict([[2300]])
print('Predicted total monthly expenses: ', prediction)