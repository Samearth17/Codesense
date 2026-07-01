import nltk
from nltk.tokenize import sent_tokenize
from nltk.classify import NaiveBayesClassifier

def analyze_sentiment(text):
    sents = sent_tokenize(text)
    neg = 0
    pos = 0
    for sentence in sents:
        sentiment_analysis = NaiveBayesClassifier.classify(sentence)
        if sentiment_analysis == 'neg':
            neg += 1
        if sentiment_analysis == 'pos':
            pos += 1
    
    if neg > pos:
        sentiment = 'negative'
    elif pos > neg:
        sentiment = 'positive'
    else:
        sentiment = 'neutral'
    
    return sentiment

# End analyze sentiment definition