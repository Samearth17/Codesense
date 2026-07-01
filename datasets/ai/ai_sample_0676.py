"""
Generate a classification model to classify spam messages using logistic regression in python
"""

# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression 

# Read the dataset
dataset = pd.read_csv('spam.csv')

# Split the dataset into features and labels
X = dataset.iloc[:, :-1].values 
y = dataset.iloc[:, -1].values

# Split the dataset into training and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

# Create a Logistic Regression model and train it
log_reg = LogisticRegression() 
log_reg.fit(X_train, y_train)

# Calculate the accuracy score
accuracy = log_reg.score(X_test, y_test)

print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(accuracy))