#Import Data
import pandas as pd
data = pd.read_csv(‘data.csv’)

#Prepare Data
X = data[['size', 'location', 'bedrooms']]
y = data['price']

#Train Model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X,y)

#Test Model
test_X = [[1500, 'downtown', 3]]
test_y = model.predict(test_X)
print(test_y)