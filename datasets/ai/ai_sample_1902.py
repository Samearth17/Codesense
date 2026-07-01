import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

# Load the dataset 
data = pd.read_csv('data.csv')

# Separate the features and labels
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Create an instance of the DecisionTreeClassifier
clf = DecisionTreeClassifier()

# Fit the model 
clf.fit(X, y)

# Make predictions 
y_pred = clf.predict(X)