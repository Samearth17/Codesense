import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# read dataset
dataset = pd.read_csv('customer_churn.csv')

# separate features(X) and labels (y)
y = dataset.churn
X = dataset.drop('churn', axis=1)

# split dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# create and train the model
model = LogisticRegression(solver='liblinear').fit(X_train, y_train)

# predict using the model
y_pred = model.predict(X_test)

# calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print('accuracy: ', accuracy)