import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Read the dataset
data = pd.read_csv('data.csv')
X = data.iloc[:, [0,1]]
y = data.iloc[:, 2] 

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Create an instance of Logistic Regression model
classifier = LogisticRegression()

# Fit the model on the training data
classifier.fit(X_train, y_train)

# Make predictions using the test data
y_pred = classifier.predict(X_test)