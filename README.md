Twitter Sentiment Analysis using Python
---------------------------------------

What is sentiment analysis?

Sentiment Analysis is the process of ‘computationally’ determining whether a piece of writing is positive, negative or neutral. It’s also known as opinion mining, deriving the opinion or attitude of a speaker.


Installation:

1. Tweepy: Python client for the official Twitter API.
// pip install tweepy
2. TextBlob: Python library for processing textual data.
// pip install textblob

3 Major steps in a program:

1. Authorize Twitter API Client.
2. Make a GET Request to Twitter API to fetch tweets for a particular query.
3. Parse the tweets. Classify each tweet as positive, negative or neutral.
   - We use sentiment.polarity method of TextBlob to get polarity between -1 to 1 and classify the tweets accordingly.
     -- if polarity > 0 => classify as "Positive"
     -- if polarity < 0 => classify as "Negative"
     -- if polarity = 0 => classify as "Neutral"
