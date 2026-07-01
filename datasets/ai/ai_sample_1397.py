import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression 

# Read the data 
data = pd.read_csv('data.csv')

# Create feature matrix 
X = data[['text', 'subject']]

# Create target vector 
y = data['label']

# Split the data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Fit the model 
logistic = LogisticRegression()
logistic.fit(X_train, y_train)

# Make predictions 
y_pred = logistic.predict(X_test)