import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def classify_sentiment(text):
 analyzer = SentimentIntensityAnalyzer()
 scores = analyzer.polarity_scores(text)

 if scores['compound'] > 0:
  return 'positive'
 elif scores['compound'] == 0:
  return 'neutral'
 else:
  return 'negative'

print(classify_sentiment('The film was terrible'))
# negative