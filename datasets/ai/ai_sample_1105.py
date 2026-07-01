import pandas as pd
import numpy as np

# import the necessary libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# define the labels and features
labels = ['positive','negative','neutral']
texts = ["I'm feeling happy today", "I'm feeling very frustrated", "I'm not sure how to feel right now"]
labels = [1,0,2]

# vectorise the texts
vectorizer = TfidfVectorizer()
features = vectorizer.fit_transform(texts)

# split the data into train and test
X = features.toarray()
Y = labels
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size = 0.8, random_state = 0)

# Create the model and fit it
model = LogisticRegression()
model.fit(X_train,Y_train)

# Make predictions
predictions = model.predict(X_test)