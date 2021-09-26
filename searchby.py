import tweepy  # https://github.com/tweepy/tweepy
import json
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

def searchtby():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    query = 'Lisa'
    language = "en"
    results = api.search_tweets(q=query, lang = language)
    for tweet in results:
        print(tweet.user.screen_name, "Tweeted:", tweet.text)


#gettweet("@taylorswift13",10)
searchtby()