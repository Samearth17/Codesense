import tweepy
from datetime import datetime

# Authentication
auth = tweepy.OAuthHandler("CONSUMER KEY",
 "CONSUMER SECRET")
auth.set_access_token("ACCESS TOKEN KEY",
 "ACCESS TOKEN SECRET")

# Connect to the API
api = tweepy.API(auth)

# Set the time (in hours) for the tweet
time = 17

# Tweet message
message = "It's time to wake up!"

# Set an infinite loop
while True:
 # Get the current time
 now = datetime.now()
 if now.hour == time:
 # Tweet the message
 api.update_status(message)
 break