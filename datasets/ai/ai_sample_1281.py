import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression 

# Load the dataset 
df = pd.read_csv('data.csv')

# Separate the target variable and input variables 
X = df.drop('SuccessProb', axis=1)
y = df['SuccessProb']

# Split data into train and test sets 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Build the logistic regression model 
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions 
predictions = model.predict_proba(X_test)