def classifySentence(sentence):
    #importing the necessary libraries
    import nltk
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    
    #Create a sentiment analyzer object
    sid_obj = SentimentIntensityAnalyzer() 
    
    #calling the polarity_scores method 
    sentiment_dict = sid_obj.polarity_scores(sentence) 
  
    #decide sentiment as positive, negative, neutral or mixed
    if sentiment_dict['compound'] >= 0.05 : 
        return "Positive"
  
    elif sentiment_dict['compound'] <= - 0.05 : 
        return "Negative"
  
    else : 
        return "Neutral"
    
result = classifySentence("She is a great teacher")
print(result)