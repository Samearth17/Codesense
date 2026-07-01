import tweepy
import json
import flask

app = flask.Flask(__name__)

CONSUMER_KEY = '<consumer key>'
CONSUMER_SECRET = '<consumer secret>'
ACCESS_TOKEN = '<access token>'
ACCESS_TOKEN_SECRET = '<token secret>'

@app.route('/tweets/string:hashtag')
def get_tweets_count(hashtag):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    tweets_count = 0
    for tweet in tweepy.Cursor(api.search, q=hashtag, rpp=100).items(100):
        tweets_count += 1
    
    response = {'count': tweets_count}
    return flask.jsonify(response)

if __name__ == '__main__':
    app.run()