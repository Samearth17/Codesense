import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR

# Import dataset
dataset = pd.read_csv('stock_prices.csv')

# Separate features (X) and target (y)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Split data into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Train the model
regressor = SVR(kernel = 'rbf', gamma = 'scale')
regressor.fit(X_train, y_train)

# Test model
y_pred = regressor.predict(X_test)