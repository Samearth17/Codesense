# Import libraries
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the data
X = np.loadtxt('data.csv', delimiter=', ',skiprows=1, usecols=[0,1])
y = np.loadtxt('data.csv', delimiter=', ', skiprows=1, usecols=[2], dtype=str)

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=5)

# Create and train the model
model = LogisticRegression().fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_pred, y_test)
print('Model accuracy:', accuracy)