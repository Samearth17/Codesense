import nltk
import random
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews

# Create a list of the tuples needed for training the model
documents = []

for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        documents.append( (list(movie_reviews.words(fileid)), category) )

# Shuffle the documents
random.shuffle(documents)

# Get all words in all documents
all_words = []

for w in movie_reviews.words():
    all_words.append(w.lower())

# Get a frequency distribution of all words
all_words = nltk.FreqDist(all_words)

# Extract the 2000 most common words
word_features = list(all_words.keys())[:2000]

# Define a function to find the 2000 most common words in a document
def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

# Create a feature set 
featuresets = [(find_features(rev), category) for (rev, category) in documents]

# Train the Naive Bayes model
training_set = featuresets[:1900]
testing_set = featuresets[1900:]

classifier = NaiveBayesClassifier.train(training_set)

# Check accuracy
print("Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(classifier, testing_set)) * 100)
classifier.show_most_informative_features(15)