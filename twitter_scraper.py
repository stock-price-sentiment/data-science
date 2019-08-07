import tweepy
from decouple import config
from sentiment import sentiment_analyzer_scores
from nltk.sentiment.vader import SentimentIntensityAnalyzer


TWITTER_AUTH = tweepy.OAuthHandler(config('TWITTER_CONSUMER_KEY'),
                                   config('TWITTER_CONSUMER_SECRET'))
TWITTER_AUTH.set_access_token(config('TWITTER_ACCESS_TOKEN'),
                              config('TWITTER_ACCESS_TOKEN_SECRET'))
TWITTER = tweepy.API(TWITTER_AUTH)

def search_tweets(keyword):
    return [status.text for status in tweepy.Cursor(TWITTER.search, q=str(keyword)).items(200) if status.text.count('$') <= 2 ]


ticker = input("What ticker?")

analyzer = SentimentIntensityAnalyzer()


tweets = search_tweets(ticker)
for tweet in tweets:
    sentiment_analyzer_scores(tweet)