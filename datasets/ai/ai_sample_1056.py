import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# get data
df = pd.read_csv('house_prices.csv')

# split the dataset into input and target variables
X = df[['square_footage', 'bedrooms', 'neighborhood']]
y = df['price']

# one-hot encode categorical variables
X = pd.get_dummies(X)

# split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# create the regressor
rf = RandomForestRegressor()

# fit the model
rf.fit(X_train, y_train)

# make predictions
y_pred = rf.predict(X_test)