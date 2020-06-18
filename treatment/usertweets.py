#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "Albin TCHOPBA"
# __copyright__ = "Copyright 2020 Albin TCHOPBA and contributors"
# __credits__ = ["Albin TCHOPBA and contributors"]
# __license__ = "GPL"
# __version__ = "3"
# __maintainer__ = "Albin TCHOPBA"
# __email__ = "Albin TCHOPBA <atchopba @ gmail dot com"
# __status__ = "Production"

import tweepy
from collections import namedtuple
import json

from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

Tweet = namedtuple("Tweet", "i id_str name text location created_at retweet_count")

def search_tweets(q):
    auth = tweepy.OAuthHandler(environ.get("CONSUMER_KEY"), environ.get("CONSUMER_SECRET"))
    auth.secure = True
    auth.set_access_token(environ.get("ACCESS_TOKEN"), environ.get("ACCESS_SECRET"))
    api = tweepy.API(auth)
    #
    i = 1
    return_dict = []
    for t in api.search(q, count=100):
        return_dict.append(
            Tweet(str(i), 
                  t._json["id_str"],
                  "<a href='http://www.twitter.com/"+ t._json["user"]["screen_name"] +"' target='_blank'>"+ t._json["user"]["name"] +"</a> ",
                  t._json["text"],
                  t._json["user"]["location"],
                  t._json["created_at"],
                  str(t._json["retweet_count"])
              ))
        i += 1
    return json.dumps(return_dict)
