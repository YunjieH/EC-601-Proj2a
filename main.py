import tweepy

from google.cloud import language_v1


# Instantiates a client
client = language_v1.LanguageServiceClient.from_service_account_json('ec602-2a-f3106761679c.json')




# assign the values accordingly
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""


# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# set access to user's access key and access secret
auth.set_access_token(access_key, access_secret)

# calling the api
api = tweepy.API(auth)

# the screen_name of the targeted user
name = ""  # set your account screen name
query = ''  # set the topic you want
language = "en"  # set language
score = 0  # initial score is 0
count = 0
for follower in api.get_follower_ids(screen_name=name):
    # this for loop will go through each follower
    results = api.search_tweets(q=query, lang=language)
    document = language_v1.Document(content=results, type_=language_v1.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
    score = score + sentiment.magnitude
    count = count + 1

avescore = score/count

print('avescore is ', avescore)
print(count, ' people talk about this topic')
