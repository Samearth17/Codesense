import pandas as pd
from sklearn.linear_model import LinearRegression

# Create
data = {'Size': [500], 
'Rooms': [4]}

df = pd.DataFrame(data)

# Train
X = df[['Size','Rooms']] 
Y = df['Price'] 
  
reg = LinearRegression().fit(X, Y) 
  
# Predict
reg.predict([[500,4]]) # Predicted price: 1715.667543