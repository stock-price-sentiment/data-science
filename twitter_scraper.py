import tweepy
from decouple import config

TWITTER_AUTH = tweepy.OAuthHandler(config('TWITTER_CONSUMER_KEY'),
                                   config('TWITTER_CONSUMER_SECRET'))
TWITTER_AUTH.set_access_token(config('TWITTER_ACCESS_TOKEN'),
                              config('TWITTER_ACCESS_TOKEN_SECRET'))
TWITTER = tweepy.API(TWITTER_AUTH)

def search_tweets(keyword):
    return [status.text for status in tweepy.Cursor(TWITTER.search, q=str(keyword)).items(200)]


ticker = input("What ticker?")

tweets = search_tweets(ticker)

print(tweets)