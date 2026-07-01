# import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# read data 
data =  pd.read_csv('data.csv')

# split data into features and labels
X = data['customer_reviews']
y = data['Popularity']

# train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

# Create Tf-idf vectorizer 
tf = TfidfVectorizer(stop_words='english')

# Fit the vectorizer to the data
tf.fit(X_train)

# Transform train and test data
X_train_tf = tf.transform(X_train)
X_test_tf = tf.transform(X_test)

# Train and fit the model
log_model = LogisticRegression()
log_model.fit(X_train_tf,y_train)

# Predict the labels
y_preds = log_model.predict(X_test_tf)

# Evaluate the model 
accuracy = accuracy_score(y_test, y_preds)

print('The model accuracy is:', accuracy)