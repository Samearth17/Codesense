import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def predict_sentiment(text):
    #Download required NLTK data
    nltk.download('vader_lexicon')
    #Create sentiment analyzer object 
    sent_analyzer = SentimentIntensityAnalyzer()
    #Predict sentiment 
    return sent_analyzer.polarity_scores(text)['compound']

# Predict sentiment of a given text
text = "This is an amazing movie!"
sentiment = predict_sentiment(text)
if sentiment >= 0.5: 
   print('Positive') 
elif sentiment == 0.0: 
   print('Neutral')
else: 
   print('Negative')