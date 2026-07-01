import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

# Preprocessing
df = pd.read_csv('transactions.csv')
X = df.iloc[:,:-1].values
y = df.iloc[:,-1].values
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Model Training
model = RandomForestRegressor()
model.fit(X, y)

# Prediction
customer_input = np.array([[10,100,5,...]]) # provide data related to past transactions
trans_scaled = scaler.transform(customer_input)
predicted_LTV = model.predict(trans_scaled)[0]
print('Predicted customer lifetime value', predicted_LTV)