#import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

#load and allocate dataset
dataset = pd.read_csv("dataset.csv")
X = dataset.Text
y = dataset.Label

#Preprocessing
cv = CountVectorizer()
X = cv.fit_transform(X)

#Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

#Model training
clf = MultinomialNB()
clf.fit(X_train,y_train)


#Evaluate the model
score = clf.score(X_test,y_test)
print("Accuracy of model: ",score)