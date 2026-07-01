import nltk
from nltk.tokenize import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentence = "This movie was extremely disappointing."

sid = SentimentIntensityAnalyzer()
sentiment = sid.polarity_scores(sentence)

if sentiment['compound'] >= 0.05:
    sentiment_label = "positive"
elif sentiment['compound'] <= - 0.05:
    sentiment_label = "negative"
else:
    sentiment_label = "neutral"

print(sentiment_label) # prints "negative"