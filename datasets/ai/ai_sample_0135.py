# Python code
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load the data set
data = pd.read_csv("customer_data.csv")

# Select features
X = data.drop(['churn'], axis=1)

# Select targets
y = data['churn']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the model
model = RandomForestClassifier()

# Train the model
model.fit(X_train, y_train)

# Make predictions and measure accuracy
predictions = model.predict(X_test)
print(model.score(X_test, y_test))