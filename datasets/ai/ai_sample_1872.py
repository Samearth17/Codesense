from textblob import TextBlob
from collections import Counter

def sentiment_analysis(sentence):
    # Tokenize the sentence
    tokens = TextBlob(sentence).words

    # Create a dictionary to store the sentiment polarity
    sentiments = Counter()
    # Calculate polarity scores and store the results
    for token in tokens:
        blob = TextBlob(token)
        sentiments[token] += blob.sentiment.polarity
    
    # Calculate total polarity 
    total = sum(sentiments.values())
    # Round to 2 decimal places 
    total = round(total, 2)
    # Assign sentiment label 
    if total > 0.2: 
        sentiment = 'Positive' 
    elif total < -0.2:
        sentiment = 'Negative' 
    else: 
        sentiment = 'Neutral'
        
    sentiment_info = {'total':total, 'sentiment': sentiment}
    return sentiment_info