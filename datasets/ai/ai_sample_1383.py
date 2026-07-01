import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {'Square Footage': [30], 'Bedrooms': [3], 'Bathrooms': [2], 'Location': ['Brooklyn']}
data = pd.DataFrame(data, columns = ['Square Footage', 'Bedrooms', 'Bathrooms', 'Location'])

train, test = train_test_split(data, test_size = 0.2)

X_train = train.iloc[:,:-1]
y_train = train.iloc[:,-1]

X_test = test.iloc[:,:-1]
y_test = test.iloc[:,-1]

regressor = LinearRegression()
regressor.fit(X_train, y_train)

predictions = regressor.predict(X_test)
test['Predicted House Price'] = predictions

print(test)