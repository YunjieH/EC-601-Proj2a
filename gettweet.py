import tweepy  # https://github.com/tweepy/tweepy
import json
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

def gettweet(a,b):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth)
    name = a

    tweetCount = b

    results = api.user_timeline(screen_name=name, count=tweetCount)

    for tweet in results:
        print(tweet.text)
        print(tweet.created_at)

gettweet("@taylorswift13",10)