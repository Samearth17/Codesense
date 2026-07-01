import tweepy

# authentication for twitter api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# create an API instance
api = tweepy.API(auth)

# search for posts with the hashtag
for tweet in tweepy.Cursor(api.search, q='#news').items(10):
 # like post
 api.create_favorite(tweet.id)
 # follow the author
 api.create_friendship(tweet.user.id)