import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Create data frame from input
df = pd.DataFrame([{
 “description”: “Gently used Apple iPhone 8 Plus, 64GB, unlocked. Great condition!”
}])

# Create feature columns
df['Length'] = df['description'].apply(len)

# Create target column
df['Sale Price'] = np.nan

# Split data into X (features) and y (target)
X = df[['Length']]
y = df['Sale Price']

# Create and fit model
model = LinearRegression()
model.fit(X, y)

# Make prediction
df.loc[0, 'Sale Price'] = model.predict(X)[0]

print('Predicted Sale Price:', df.loc[0, 'Sale Price'])