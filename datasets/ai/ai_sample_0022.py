import numpy as np
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

# Read in the data
data = pd.read_csv('reviews.csv')

# Tokenise the texts
data['tokenised'] = data['review'].apply(word_tokenize)

# Remove stopwords
stop_words = set(stopwords.words('english'))
data['filtered'] = data['tokenised'].apply(lambda x: [val for val in x if val not in stop_words])

# Normalize words
wordnet_lemmatizer = WordNetLemmatizer()
data['normalised'] = data['filtered'].apply(lambda x: [wordnet_lemmatizer.lemmatize(val) for val in x])

# Generate features using CountVectorizer
cv = CountVectorizer()
data['features'] = cv.fit_transform(data['normalised'].astype('str')).toarray()

# Split into training and test sets
X = data['features']
y = data['sentiment']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = MultinomialNB(alpha=0.1)
model.fit(X_train, y_train)

# Predict using the test set
predictions = model.predict(X_test)

# Generate a classification report
report = classification_report(y_test, predictions)
print(report)