import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load the Iris dataset
dataset = datasets.load_iris()

# Creating a feature matrix
X = dataset.data

# Creating a target vector
y = dataset.target

# Splitting data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state = 0)

# Training a Naive Bayes classifier
clf = GaussianNB()
clf.fit(X_train, y_train)

# Making predictions
y_pred = clf.predict(X_test)

# Checking the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)