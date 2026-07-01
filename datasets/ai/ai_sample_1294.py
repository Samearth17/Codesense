import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

# load data
iris = load_iris()
X = iris.data
y = iris.target

# split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Training
dtree_model = DecisionTreeClassifier(max_depth=2).fit(X_train, y_train)

# Testing
dtree_predictions = dtree_model.predict(X_test)

# Checking accuracy
print("Accuracy:",np.mean(dtree_predictions==y_test))