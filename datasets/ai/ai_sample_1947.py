import nltk
import sklearn

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

sentence = 'The interface is very intuitive and user-friendly.'

# Tokenize the sentence
tokens = nltk.word_tokenize(sentence)

# Get the features from the tokens
count_vect = CountVectorizer()
word_count = count_vect.fit_transform(tokens)

# Create a Multinomial Naive Bayes classifier
clf = MultinomialNB().fit(word_count, ['positive'])

# Predict the sentiment of the sentence
prediction = clf.predict(word_count)

# Print the result
print(f'The sentiment of the sentence is {prediction[0]}.')