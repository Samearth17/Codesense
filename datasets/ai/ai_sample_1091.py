"""
Classify a sentence as 'positive' or 'negative
"""

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def classify_sentence(sentence):
    sid = SentimentIntensityAnalyzer()
    sentiment = sid.polarity_scores(sentence)
    if sentiment['compound'] >= 0.05:
        return 'positive'
    elif sentiment['compound'] <= - 0.05:
        return 'negative'
    else:
        return 'neutral'

if __name__ == '__main__':
    sentence =  "The movie was great!"
    classification = classify_sentence(sentence)
    print(classification)