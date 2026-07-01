import re
import nltk

def classify_sentiment(tweet_text):
    tokens = nltk.word_tokenize(tweet_text)
    sentiment_scores = 0

    # Calculate sentiment score
    for token in tokens:
        if token in POSITIVE_WORDS:
            sentiment_scores += 1
        elif token in NEGATIVE_WORDS:
            sentiment_scores -= 1

    # Classify sentiment
    if sentiment_scores > 0:
        return "positive"
    elif sentiment_scores == 0:
        return "neutral"
    else:
        return "negative"