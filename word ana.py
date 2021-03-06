from google.cloud import language_v1


# Instantiates a client
client = language_v1.LanguageServiceClient.from_service_account_json('ec602-2a-f3106761679c.json')

# The text to analyze
text = 'nice food'
document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment

print("Text: {}".format(text))
print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))