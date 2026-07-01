def sentiment_analysis(tweets):
    # Initialize a list to store the result 
    results = [] 

    # Iterate through each tweet
    for tweet in tweets:
        # Clean the tweet 
        tweet = preprocessing(tweet)

        # Vectorize the tweet and obtain the prediction 
        tweet_vector = vectorize(tweet)
        prediction = predict_sentiment(tweet_vector)

        # Append the prediction to the result list
        if prediction == 1:
            results.append("Positive")
        elif preduction == 0:
            results.append("Negative")

    return results