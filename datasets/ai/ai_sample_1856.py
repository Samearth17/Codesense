"""
Program to predict the quality of a text using supervised learning
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC

#Load the training dataset
train_data = pd.read_csv("data")

#Preprocess the data by creating features using CountVectorizer
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(train_data['text'])
Y_train = train_data['quality']

#Train the model
model = SVC()
model.fit(X_train, Y_train)

#Test the model
test_data = "This is a sample text"
X_test = vectorizer.transform([test_data])
prediction = model.predict(X_test)

print('Predicted Quality: %s' % prediction[0])