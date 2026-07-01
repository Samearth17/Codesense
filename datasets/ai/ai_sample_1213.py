# Install packages
import tweepy
import requests

# Access Twitter API
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'

access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Set up authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_token_secret)

# Set up the API
api = tweepy.API(auth)

# Retrieve information
username = "@twitter"
user = api.get_user(username)

print("Name: "+user.name)
print("Location: "+user.location)
print("Followers count: "+str(user.followers_count))
print("Profile picture: "+user.profile_image_url)