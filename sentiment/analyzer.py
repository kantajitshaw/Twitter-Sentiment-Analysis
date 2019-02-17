import tweepy
from textblob import TextBlob

consumer_key = "<YOUR_TWITTER_CONSUMER_KEY>"
consumer_secret = "<YOUR_TWITTER_CONSUMER_SECRET>"

access_token = "<YOUR_TWITTER_ACCESS_TOKEN>"
access_token_secret = "<YOUR_TWITTER_ACCESS_TOKEN_SECRET>"

auth = tweepy.OAuthHandler (consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def analyze(query_text):
    public_tweets = api.search('#'+query_text)
    result = []
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        result.append((tweet.text, analysis.sentiment))
    return result
