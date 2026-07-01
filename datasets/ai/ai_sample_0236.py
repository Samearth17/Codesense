import os
import tweepy
from django.shortcuts import render

# Create your views here.
def index(request):
    consumer_key = os.environ['TWITTER_CONSUMER_KEY']
    consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
    access_key = os.environ['TWITTER_ACCESS_KEY']
    access_secret = os.environ['TWITTER_ACCESS_SECRET']
 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
 
    hashtags = ["#python"]
    tweets = api.search(q=hashtags, lang='en')
 
    args = {'tweets': tweets}
    return render(request, 'index.html', args)