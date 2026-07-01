import nltk
 from nltk.sentiment.vader import SentimentIntensityAnalyzer 
 
sid = SentimentIntensityAnalyzer()

def predict_sentiment(tweet):
 scores = sid.polarity_scores(tweet)
 if scores['compound'] >= 0.5:
 return 'Positive'
 elif scores['compound'] <= -0.5:
 return 'Negative'
 else:
 return 'Neutral'
 
tweet = "I am feeling positive about life today!"

print(predict_sentiment(tweet))
# Output: Positive