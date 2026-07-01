import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix

# Load data 
data = pd.read_csv('data.csv')

# Separate labels and features
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Split the dataset into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = MultinomialNB()
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = model.score(X_test, y_test)
print('Model accuracy is:', round(accuracy*100, 2), '%', sep='')

# Print confusion matrix
cm = confusion_matrix(y_test, y_pred)
print('Confusion matrix:')
print(cm)