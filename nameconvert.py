import tweepy  # https://github.com/tweepy/tweepy
import json
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_key, access_secret)


api = tweepy.API(auth)

# using get_user with id
_id = "103770785"
user = api.get_user(id = _id)

print("The id " + _id +
      " corresponds to the user with the name : " +
      user.name)