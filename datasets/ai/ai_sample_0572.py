import nltk
from nltk.classify import NaiveBayesClassifier

# Define the training set
reviews_train = [('The food was amazing!', 'positive'),
 ('I was not happy with the customer service.', 'negative'),
 ('The quality of the food was fantastic!', 'positive')]

# Train Naive Bayes Classifier
classifier = NaiveBayesClassifier.train(reviews_train)

# Make Predictions
reviews_test = ['The food was not good.']
prediction = classifier.classify(reviews_test)

print('Predicted sentiment is:', prediction)