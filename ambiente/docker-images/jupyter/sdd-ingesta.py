#!/usr/bin/python
# -*- coding: utf-8 -*-

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import time
import sys
import tweepy
from textblob import TextBlob
from datetime import datetime

# Llaves de usuario de Twitter, se generan en dev.twitter.com

consumer_key = '7mIyn18IftHTQUDUI4QDfBPoG'
consumer_secret = 'wz4cagoX3DJ95VVsjo5djdVcxv1ZdYZ2RFdkNCZVT2YvIlgRZM'
access_token = '425496873-yKrqqxkSxxpwc433ARfXyYLwbgfE3yR4PLm8wtnR'
access_token_secret = 'stPZZKpiyD6BIAtko7FJJYg0tqmhxw2YaSKBGr9upeJYC'

class TweepyFileListener(tweepy.StreamListener):

    def on_data(self, data):
        print ("on_data called")

        # Decodificamos ya que Twitter escupe JSON

        decoded = json.loads(data)
        usrid = '%s' % decoded['id']
        tweet = TextBlob(decoded['text'])

        # Se determina si el sentimiento es positivo, negativo, or neutral

        if tweet.sentiment.polarity < -.5:
            sentiment = 'muy negativo'
        elif tweet.sentiment.polarity < .0 and tweet.sentiment.polarity \
            > -.5:
            sentiment = 'negativo'
        elif tweet.sentiment.polarity == 0:
            sentiment = 'neutral'
        elif tweet.sentiment.polarity < .5 and tweet.sentiment.polarity \
            > 0:
            sentiment = 'positivo'
        else:
            sentiment = 'muy positivo'

        polarity = '%s\n' % str(tweet.sentiment.polarity)

        #Validamos las cadenas vacias
        if len(tweet) < 0:
            sentiment="nvl"
            polarity="nvl"

        # Grabamos en archivo .txt tipo log solo los features seleccionados

        with open('EASentiment.psv', 'a') as tweet_log:

            # print ("Received: %s\n") % msg, no sirve el %, entonces se trae la info con .format

            print ('Received: {}'.format(usrid))
            tweet_log.write(usrid + '|' + sentiment + '|'
                            + polarity)

        # Grabamos en archivo .txt los Tweets en formato Orig Json

        with open('EARaw.json', 'a') as tweet_log:

            # print ("Received: %s\n") % msg, no sirve el %, entonces se trae la info con .format
            # print ("Received: {}".format(msg))

            tweet_log.write(data)

if __name__ == '__main__':
    l = TweepyFileListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    print ("Mostrando los nuevos tweets de #EgyptAir:")

        # Se baja la info con las siguientes opciones visuales de streaming

    stream = tweepy.Stream(auth, l)
    stream.filter(track=['EgyptAir'])
