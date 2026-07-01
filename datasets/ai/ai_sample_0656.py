import pandas as pd
from sklearn import datasets
from sklearn import tree

data = pd.read_csv('data.csv')

# Split the data
X = data.drop('target', axis=1)
y = data['target']

# Train the model
clf = tree.DecisionTreeClassifier()
clf.fit(X, y)

# Test the model
y_pred = clf.predict(X)

# Evaluate accuracy
accuracy = metrics.accuracy_score(y, y_pred)
print('Accuracy:', accuracy)