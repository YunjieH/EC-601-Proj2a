# EC-601-Proj2
Yunjie Huang
U70536658
Section A1

## Function 1 named gettweet(a,b)
This founction have 2 inputs.
 a is name.
 b is number of tweets.
 This function will returen a's b newest tweets(only text and created time).

## Function 2 named searchby()
This function is main focuse on search_tweets() in the tweepy.
This function can set up perfered language, and search the tweets have the key word we want.
This py scrip will return the tweets text with the key word.
And it also have some parameter can setup the time interval. 

## Function 3 named nameconvert()
In the Twiter each user will have three names: id user_id and screen_name.
This function is use to convert between this three name.
In another word, if we know one of three name, we can get other two names by this function.

## function4 word ana
This file is a test of google NLP api. I usde google NLP to analyze natural language. The text i use is 'nice food'.
The result is 0.899, which is very positive.


## user story
Tweeter channel host can know what is the altitude his followers have with the topic he want to post.
When channel host have a new topic want to post. He can check the altitude score. The score is between -1 to 1. 1 is the most positive score.

## main Functin
In this function, the channel host need set up channels name and the topic he want to check.
Then this function will go through all his followers.
For each follower this function will take out the tweet relate to this topic, and then use google NLP determin the altitude.
At last this function will returen the average altitude score and the number of tweets relate to the topic

## unit test: wrongkey
This function is test the keyword not exist. if the keyword is not exist, there will no text pass to NLP. So the count will be 0. This will cause a problem at avescore = score/count

## unit test: wronglan
This is test with wrong Language code. api.search_tweets can't handel wrong Language code, there will be an error.

## unit test: wrongname
This is test with the name not exist. error massage about user not exit will appear.
