import requests
import praw
from textblob import TextBlob

# Initializing the Reddit instance
reddit = praw.Reddit(client_id=YOUR_CLIENT_ID,
 client_secret=YOUR_CLIENT_SECRET,
 user_agent='YOUR_USER_AGENT')

# Inputting the subreddit to analyze
subreddit = reddit.subreddit("AskReddit")

# Getting the 50 top posts
posts = subreddit.top(limit=50)

# Iterating over the posts
for post in posts:
 # Fetching the post data
 post_data = requests.get(url=post.url).json()
 
 # Calculating the sentiment 
 sentiment = TextBlob(post_data['data']['title']).sentiment
 
 # Printing the sentiment
 print('Post Title: {0} --> Sentiment: {1}'.format(post_data['data']['title'], sentiment))