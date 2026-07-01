# import required modules
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# read in data
dataframe = pd.read_csv('loan_data.csv')

# define feature and target labels
X = dataframe.loc[:, dataframe.columns != 'loan_status']
y = dataframe.loan_status

# split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

# create a model
model = RandomForestClassifier()

# train the model
model.fit(X_train, y_train)

# make predictions on the test set
predictions = model.predict(X_test)