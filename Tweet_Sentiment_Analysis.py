import tweepy
from textblob import TextBlob
import numpy as np


"""Authentication"""
consumer_key= 'CONSUMER_KEY_HERE'
consumer_secret= 'CONSUMER_SECRET_HERE'

access_token='ACCESS_TOKEN_HERE'
access_token_secret='ACCESS_TOKEN_SECRET_HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

""" Preparing query features """
#List of keywords to be searched in the 
keywords = ['Antonio Conte']
#Hashtag related to the topic
hashtag = "CFC" 
#Dates to give a timeline for the searches
since = "2017-06-18"
until = "2017-06-19"


""" Retrieving Tweets and saving them in a csv file """
all_polarities = dict()
for candidate in keywords:
	this_candidate_polarities = []


""" Search Query """	
search_tweets = api.search(q=[keywords, hashtag], count= 50, since = since, until=until)
	
"""  Save the tweets in csv file """
with open('twitter_sentiment.csv', 'w') as file:
	write_in_file = csv.writer(file)
	write_in_file.writerow(['Index', 'Tweet', 'Author', 'Sentiment'])

	for i, tweet in enumerate(search_tweets):
		analysis = TextBlob(tweet.text)
		author = tweet.user.screen_name

		polarity = analysis.sentiment.polarity
		row_to_add = str(i+1) + ',' + tweet.text + ',' + author + ','

		if polarity > 0:
			file.write(row_to_add + 'Positive')
			file.write('\n')
		elif polarity == 0:
			file.write(row_to_add + 'Neutral')
			file.write('\n')
		else:
			file.write(row_to_add + 'Negative')
			file.write('\n')