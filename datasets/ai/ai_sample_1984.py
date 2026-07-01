import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Read the data
data = pd.read_csv('cars.csv')

# Split the data in features (X) and labels (y)
X = data.drop('price', axis=1)
y = data['price']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) 

# Train the model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Predict the price of the cars in the test set
y_pred = model.predict(X_test)

# Compare the predictions with the actual values
for prediction, actual in zip(y_pred, y_test):
 print(prediction, actual)