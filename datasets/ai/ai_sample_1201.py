import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load data
data = pd.read_csv("data.csv")

# Split data into training and test sets
X = data[['height', 'weight']]
y = data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate model
score = model.score(X_test, y_test)
print("Model Accuracy: {:.2f}".format(score))