import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the data
df = pd.read_csv('sentiment.csv')

# Transform the text into numerical features
cv = CountVectorizer(stop_words='english')
X = cv.fit_transform(df['text'])
y = df['sentiment']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, test_size=.3)

# Train the model
nb = MultinomialNB()
nb.fit(X_train, y_train)

# Make predictions
y_pred = nb.predict(X_test)

# Evaluate the model
score = accuracy_score(y_test, y_pred)
print(score)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))