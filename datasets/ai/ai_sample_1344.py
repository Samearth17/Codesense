import nltk 
import random 
from nltk.corpus import movie_reviews 

# Generate a set of documents
documents = [(list(movie_reviews.words(fileid)), category) 
             for category in movie_reviews.categories() 
             for fileid in movie_reviews.fileids(category)]

# Shuffle the documents
random.shuffle(documents)

# Generate features
all_words = []
for w in movie_reviews.words():
   all_words.append(w.lower())

all_words = nltk.FreqDist(all_words) 

word_features = list(all_words.keys())[:3000] 

# Function to create a dictionary of features for each review in the list documents
# The keys are the words in word_features
# The values of each key are either true or false for whether that feature appears in the review 
def find_features(document):
 features = {}
 words = set(document)
 for w in word_features:
     features[w] = (w in words)
 
 return features

#Find the features for all the documents
featuresets = [(find_features(rev), category) for (rev, category) in documents] 

#Create the training set using the featuresets
training_set = featuresets[:1900] 

# Create the testing set using the featuresets
testing_set = featuresets[1900:] 

# Train the classifier
classifier = nltk.NaiveBayesClassifier.train(training_set)

#Test the classifier and print the accuracy
print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)