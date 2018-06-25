# write your code here
# usage should be python3 part1.py <username> <num_tweets>
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
For SI 507 Waiver, fall 2018
@author: oshinnayak, onayak @umich.edu
"""

import tweepy
import nltk 
import json
import sys
import requests_oauthlib
import webbrowser
from tweepy import OAuthHandler
from nltk.corpus import stopwords
import string
import re
from nltk import FreqDist
 


def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

def printResults(list_common, word_type):
	result_string = []
	for item in list_common:
		word = str(item[0]) + "(" + str(item[1]) + ")"
		result_string.append(word)
	print(word_type + ' '.join(result_string))
	
# Get these from the Twitter website, by going to
# https://apps.twitter.com/ and creating an "app"
# Don't fill in a callback_url; instead, put in a placeholder for the website
# Visit the Keys and Access Tokens tab for your app and grab the following two values

client_key = 'ED8Kqy69o2EZskqDQkTvF2mVk' # what Twitter calls Consumer Key -- fill in a string here
client_secret = 'jHImUlSHvVls9ga27yZ1AZSeNTgH60GacVVfUCZF9b4FKthFkp' # What Twitter calls Consumer Secret -- fill in a string here
access_token= '1005972017642856448-hg6gqTpnt3bGZUIIBNnGIIz1lNZnCW'
access_secret= 'kof2bjcQUKqqXGcYZYAI8dXbK3UkEj5kuDZ6tRWM6eBkU'

if not client_secret or not client_key:
    print("You need to fill in client_key and client_secret. See comments in the code around line 8-14")
    exit()

auth = OAuthHandler(client_key, client_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

username = sys.argv[1]
number_of_tweets = sys.argv[2]

print("USER: " + username)

#Get the tweets
tweets_analyzed = api.user_timeline(screen_name = username, count = int(number_of_tweets), tweet_mode="extended", include_rts=True)

print("TWEETS ANALYZED: " + str(len(tweets_analyzed)))

tweets = [tweet.full_text for tweet in tweets_analyzed]

tokens = nltk.word_tokenize(' '.join(tweets))

#Removing Stop Words
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via', 'RT', 'https', 'http']
terms_stop = [term for term in tokens if ((term not in stop) and (len(term)>1) and (term[0] != "'"   ) and (re.search('[a-zA-Z]', term)) and (not re.search('^HTT', term)) and (not re.search('^htt', term)))]

terms_tagged = nltk.pos_tag(terms_stop)

tok_verbs = [term_tagged[0] for term_tagged in terms_tagged if term_tagged[1].startswith('VB')]
tok_nouns = [term_tagged[0] for term_tagged in terms_tagged if term_tagged[1].startswith('NN')]
tok_adjs = [term_tagged[0] for term_tagged in terms_tagged if term_tagged[1].startswith('JJ')]
   
 
printResults(FreqDist(tok_verbs).most_common(5),"VERBS: ")
printResults(FreqDist(tok_nouns).most_common(5),"NOUNS: ")
printResults(FreqDist(tok_adjs).most_common(5),"ADJECTIVES: ")



#print(json.dumps(tweets_analyzed[0]._json, indent=4, sort_keys=True))
#print(tweets_analyzed[0].retweeted)

originalTweets = api.user_timeline(screen_name = username,count = int(number_of_tweets),tweet_mode="extended",include_rts=False)

print("ORIGINAL TWEETS: " + str(len(originalTweets)))

tweet_fav = [tweet.full_text for tweet in originalTweets if tweet.favorite_count]

print("TIMES FAVORITED (ORIGINAL TWEETS ONLY): " + str(len(tweet_fav)))

tweet_org_retweet = [tweet.full_text for tweet in originalTweets if tweet.retweet_count]

print("TIMES RETWEETED (ORIGINAL TWEETS ONLY): " + str(len(tweet_org_retweet)))


#write to csv 

# Open/create a file to append data to
csvFile = open('noun_data.csv', 'a')
csvFile.write('Noun,Number\n')

for (text, count) in FreqDist(tok_nouns).most_common(5):
    writeString = ""
    writeString = str(text)+","+str(count) + "\n"
    csvFile.write(writeString)

csvFile.close()




