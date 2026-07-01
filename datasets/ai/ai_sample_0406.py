import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer 

sid = SentimentIntensityAnalyzer() 
  
text = "This movie was truly amazing"

sentiment_scores = sid.polarity_scores(text) 

if sentiment_scores['compound'] >= 0.05 : 
    print("Positive") 
elif sentiment_scores['compound'] <= - 0.05 : 
    print("Negative")
else : 
    print("Neutral")