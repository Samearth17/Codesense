import tweepy

# Replace the API_KEY and API_SECRET with your application's key and secret.
auth = tweepy.AppAuthHandler(API_KEY, API_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True,
 wait_on_rate_limit_notify=True)

# Replace the hashtag with your hashtag of interest.
hashtag = '#100DaysOfCode'

# Fetch the tweets
tweets = tweepy.Cursor(api.search, q=hashtag, lang="en").items()

# Print out the tweets
for tweet in tweets:
 print(tweet.text)