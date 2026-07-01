def identify_sentiment(sentence):
    # Split sentence into individual words
    words = sentence.split()

    # Import Textblob package
    from textblob import TextBlob

    # Create a textblob object
    analysis = TextBlob(' '.join(words))

    # Return sentiment polarity 
    return analysis.sentiment.polarity
    
    
if __name__ == "__main__":
    sentiment = identify_sentiment('I'm feeling great today')
    if sentiment > 0:
        print('Positive sentiment')
    elif sentiment == 0:
        print('Neutral sentiment')
    else:
        print('Negative sentiment')