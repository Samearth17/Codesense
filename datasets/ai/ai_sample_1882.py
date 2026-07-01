"""
Python script to download tweets from a given list of twitter accounts.
"""

import tweepy

def get_tweets(accounts):
    # Authenticate with twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Get the latest tweets 
    all_tweets = []
    for account in accounts:
        tweets = api.user_timeline(screen_name=account, count=10)
        all_tweets.extend(tweets)
    
    # Return the tweets as a list of dictionaries
    return [tweet._json for tweet in all_tweets]

if __name__ == '__main__':
    accounts = ['USER1', 'USER2', 'USER3']
    tweets = get_tweets(accounts)
    print(tweets)