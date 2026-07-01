import numpy as np
from sklearn.naive_bayes import BernoulliNB

def predict_sentiment(clf, features):
    # Predict the sentiment from features using the Naive Bayes classifier
    return clf.predict(features)

def train_naive_bayes(features, labels):
    """
    Train a Naive Bayes classifier on a set of features and labels
    
    :param features: The array of features
    :param labels: The corresponding labels
    :return: A trained Naive Bayes classifier
    """
    
    # Create a Bernoulli Naive Bayes classifier
    clf = BernoulliNB()
    # Train the classifier
    clf.fit(features, labels)
    
    return clf

def extract_features_from_sentences(sentences):
    """
    Extract features from sentences
    
    :param sentences: An array of sentences
    :return: Array of feature vectors for each sentence
    """
    # Get the length of each sentence
    len_features = [len(sentence.split()) for sentence in sentences]
    # Return the feature vector containing the lengths of each sentence
    return np.array([len_features])