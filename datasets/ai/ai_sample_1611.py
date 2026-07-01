# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Read in the auto dataset
df = pd.read_csv('auto.csv')

# Get the features and labels
X = df.drop(columns='mpg')
y = df['mpg']

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the linear regressor
lr = LinearRegression()

# Train the model
lr.fit(X_train,y_train)

# Get the predictions
preds = lr.predict(X_test)

# Calculate the R2 score
r2 = r2_score(y_test, preds)