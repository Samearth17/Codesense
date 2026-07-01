import pandas as pd

df = pd.read_csv('email_dataset.csv')

#Create feature vectors
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['email'])

#Train the data with Naive Bayes
from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
model.fit(X, df['label'])

#Test the model
spam_predictions = model.predict(X)
print(spam_predictions)