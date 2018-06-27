#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 20:53:24 2018

@author: anaghakelkar
"""

import re
import tweepy
from textblob import TextBlob

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def get_tweet_sentiment(api, tweet):
    analysis=TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity>0:
        return 'positive'
    elif analysis.sentiment.polarity==0:
        return 'neutral'
    else:
        return 'negative'

def get_tweets(api, query, count=10):
    tweets=[]
    try:
        fetched_tweets = api.search(q=query, count=count)
        for tweet in fetched_tweets:
            parsed_tweet={}
            parsed_tweet['text']=tweet.text
            parsed_tweet['sentiment']=get_tweet_sentiment(api, tweet.text)
            if tweet.retweet_count>0:
                if parsed_tweet in tweets:
                    tweets.append(parsed_tweet)
            else:
                tweets.append(parsed_tweet)
        return tweets
    except tweepy.TweepError as e:
        print("Error : "+str(e))

def main():
    # keys and tokens
    consumer_key = 'QpEjHBUbFYDl1bBZJcL7KhqMg'
    consumer_secret = 'fcu1ifBO9DBgGQQvH4cXcTAe5hNAliFAW4VoeY7wvRK71sq0zV'
    access_token = '979508319910940672-map4j3edYz2QsC2uWOFgIUfMk6yTEFq'
    access_secret = 'GGxixKqHQctYPcU3u7y0qkf8G8Pg5VEJFE65i8OhAc8eP'
    # attempt authentication
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        api = tweepy.API(auth)
    except:
        print("Error: Authentication failed")
    tweets = get_tweets(api, query='I love my job.', count=200)
    # picking positive tweets from tweets
    ptweets=[tweet for tweet in tweets if tweet['sentiment']=='positive']
    # picking negative tweets from tweets
    ntweets=[tweet for tweet in tweets if tweet['sentiment']=='negative']
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
    print("Neural tweets percentage: {} %".format(100*(len(tweets)-len(ptweets)-len(ntweets))/len(tweets)))
    # printing first 5 positive tweets
    print("\n\nPositive tweets:")
    for tweet in ptweets[:10]:
        print(tweet['text'])
    # printing first 5 negative tweets
    print("\n\nNegative tweets:")
    for tweet in ntweets[:10]:
        print(tweet['text'])

if __name__=="__main__":
    main()
