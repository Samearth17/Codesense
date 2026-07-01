from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

# Create a TextBlob object using the NaiveBayesAnalyzer
sentiment_analyzer = TextBlob(analyzer=NaiveBayesAnalyzer())

# Method to predict the sentiment of a given sentence
def predict_sentiment(sentence):
    # Get the polarity score of the sentence
    polar_score = sentiment_analyzer.sentiment.polarity
    # class the sentiment of the given sentence
    if polar_score > 0:
        sentiment = "positive"
    elif polar_score == 0:
        sentiment = "neutral"
    else:
        sentiment = "negative"
    # Print out the sentiment of the given sentence
    print("The sentiment of the given sentence is:", sentiment)

sentence = "This movie is amazing!"
predict_sentiment(sentence)