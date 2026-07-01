import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load the Iris dataset
X, y = load_iris(return_X_y=True)

# Create a training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=21, stratify=y)

# Fit the model using K-Nearest Neighbors classifier
knn = KNeighborsClassifier(n_neighbors=8)
knn.fit(X_train, y_train)

# Make predictions on the test set
y_pred = knn.predict(X_test)