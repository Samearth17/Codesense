import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
  
def sentiment_calculator(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)
    if sentiment_scores['compound'] >= 0.5:
        sentiment = 'positive'
    elif -0.5 < sentiment_scores['compound'] < 0.5:
        sentiment = 'neutral'
    else:
        sentiment = 'negative'
    return sentiment
  
sentence = 'This is an amazing experience!'
sentiment_calculator(sentence)
# Output: 'positive'