import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
from elasticsearch import Elasticsearch
import re

# import twitter keys and tokens
from config import *

# create instance of elasticsearch
es = Elasticsearch()


class TweetStreamListener(StreamListener):

    # on success
    def on_data(self, data):

        # decode json
        dict_data = json.loads(data)

        # pass tweet into TextBlob
        tweet = TextBlob(dict_data["text"])

    print "Tweet captured - ID: " + str(dict_data["id"])

        # output sentiment polarity
        print "Polarity: " + str(tweet.sentiment.polarity)

        # determine if sentiment is positive, negative, or neutral
        if tweet.sentiment.polarity < 0:
            sentiment = "negative"
        elif tweet.sentiment.polarity == 0:
            sentiment = "neutral"
        else:
            sentiment = "positive"

        # output sentiment
        print "Sentiment: " + sentiment

    cleanText = re.sub(r'^https?:\/\/.*[\r\n]*', '', dict_data["text"], flags=re.MULTILINE)
    cleanText = re.sub(r'^http?:\/\/.*[\r\n]*', '', cleanText, flags=re.MULTILINE)
    print cleanText

        # add text and sentiment info to elasticsearch
        es.index(index="tweetsuio",
                 doc_type="test-type",
                 body={"author": dict_data["user"]["screen_name"],
                       "date": dict_data["created_at"],
                       "tweet": dict_data["text"],
               "text": cleanText,
                       "polarity": tweet.sentiment.polarity,
                       "subjectivity": tweet.sentiment.subjectivity,
                       "sentiment": sentiment})
    print "Successfuly stored on ElasticSearch!"
    print "------------------------------------"

        return True

    # on failure
    def on_error(self, status):
        print status

if __name__ == '__main__':

    # create instance of the tweepy tweet stream listener
    listener = TweetStreamListener()

    # set twitter keys/tokens
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # create instance of the tweepy stream
    stream = Stream(auth, listener)

    # search twitter for "congress" keyword
    stream.filter(locations=[-78.586922,-0.395161,-78.274155,0.021973])