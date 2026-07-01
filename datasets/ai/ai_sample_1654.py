import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Read and preprocess the data
dataset = pd.read_csv('train.csv')

vectorizer = TfidfVectorizer()
x_train = vectorizer.fit_transform(dataset['text'])
y_train = dataset['label']

# Train the model
model = MultinomialNB().fit(x_train, y_train)

# Test the model
x_test = vectorizer.transform(test_data['text'])
predictions = model.predict(x_test)