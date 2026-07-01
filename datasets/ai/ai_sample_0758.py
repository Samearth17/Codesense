import tweepy

# Set up API access for your application
consumer_key = "<your_consumer_key>"
consumer_secret = "<your_consumer_secret>"
access_token = "<your_access_token>"
access_token_secret = "<your_access_token_secret>"

# Create the API access object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get the user's timeline
user_timeline = api.user_timeline('username', count=5)

# Print each tweet
for tweet in user_timeline:
    print(tweet.text)