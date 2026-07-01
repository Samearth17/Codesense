import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
  
sid = SentimentIntensityAnalyzer() 
  
# Function to get the sentiment 
def sentiment_scores(sentence): 
    print(sentence)
    score = sid.polarity_scores(sentence) 
    print("Overall sentiment for the text : ", score) 
  
# Driver code 
if __name__ == "__main__": 
   
    # Input text for sentiment scoring 
    sentence = "This is an amazing product!"
  
    sentiment_scores(sentence)