import numpy as np
import sklearn as sk
from sklearn import datasets

# Load the data
iris = datasets.load_iris()

# Split the data into train and test sets
X_train, X_test, y_train, y_test = sk.model_selection.train_test_split(
 iris.data, iris.target, test_size=0.3, random_state=0)

# Create and fit the model
clf = sk.neighbors.KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)

# Predict with the test set
y_pred = clf.predict(X_test)

# Check the accuracy
print("Accuracy: {0:.2f}".format(sk.metrics.accuracy_score(y_test, y_pred)))