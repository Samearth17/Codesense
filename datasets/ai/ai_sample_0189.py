# Load libraries
import pandas as pd
import numpy as np

# Load data
data = pd.read_csv("stockdata.csv")

# Split data
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Train/Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Decision Tree Model
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(criterion='entropy', random_state=0)
clf.fit(X_train, y_train)

# Model Accuracy
y_pred = clf.predict(X_test)
print('Model accuracy: ',clf.score(X_test, y_test))