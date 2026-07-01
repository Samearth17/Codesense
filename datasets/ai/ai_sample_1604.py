import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Prepare data
train_data = # your train data
train_labels = # your train label
test_data = # your test data

# Build a bag of words model
vectorizer = CountVectorizer(stop_words=stopwords.words('english'))
train_data_features = vectorizer.fit_transform(train_data)

# Train a Naive Bayes classifier
nb_classifier = MultinomialNB().fit(train_data_features, train_labels)

# Test the classifier
test_data_features = vectorizer.transform(test_data)
predictions = nb_classifier.predict(test_data_features)