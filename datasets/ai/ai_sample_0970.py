import tweepy
from textblob import TextBlob

consumer_key='XXXX'
consumer_secret='XXXX'

access_token='XXXX'
access_token_secret='XXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search(q='Python programming')

for tweet in public_tweets:
 print(tweet.text)
 analysis = TextBlob(tweet.text)
 print(analysis.sentiment)