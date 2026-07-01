import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def classify_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    score = sid.polarity_scores(text)
    if score['compound'] >= 0.05:
        return 'positive'
    elif score['compound'] <= - 0.05:
        return 'negative'
    else:
        return 'neutral'

sentiment = classify_sentiment("The government has done a tremendous job in handling the pandemic situation.")
print(sentiment)
# Output: positive