import numpy as np
import pandas as pd
from sklearn import tree

# Load the dataset
data = pd.read_csv("data.csv")

# Create target variable
target = data["target"]

# Create feature variables
features = data.drop(columns = ["target"])

# Create decision tree model
model = tree.DecisionTreeClassifier()
model.fit(features, target)