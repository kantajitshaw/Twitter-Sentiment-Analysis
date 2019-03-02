import os

import tweepy
from textblob import TextBlob
from sentiment_analyzer.configparser import load_config
from sentiment_analyzer.settings import BASE_DIR

config = load_config(os.path.join(BASE_DIR, 'sentiment.ini'))

consumer_key = config['twitter_config.consumer_key']
consumer_secret = config['twitter_config.consumer_key_secret']

access_token = config['twitter_config.access_token']
access_token_secret = config['twitter_config.access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def analyze(query_text):
    public_tweets = api.search('#'+query_text)
    result = []
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        result.append((tweet.text, analysis.sentiment))
    return result
