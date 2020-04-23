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
import config


def search_tweets(q):
    auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.secure = True
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)
    api = tweepy.API(auth)
    #
    return_html = ("<br/><h3>Résultats</h3>"
       "<table border='1'>"
            "<tr>"
                "<td></td>"
                "<td>id str</td>"
                "<td>username</td>"
                "<td>text</td>"
                "<td>location</td>"
                "<td>created at</td>"
                "<td>nb retweet</td>"
            "</tr>"    
    "")
    #
    i = 1
    for t in api.search(q, count=100):
        return_html += (""
            "<tr>"
                "<td>"+ str(i) +"</td>"
                "<td>"+ t._json["id_str"] +"</td>"
                "<td><a href='http://www.twitter.com/"+ t._json["user"]["screen_name"] +"' target='_blank'>"+ t._json["user"]["name"] +"</a> </td>"
                "<td>"+ t._json["text"] +"</td>"
                "<td>"+ t._json["user"]["location"] +"</td>"
                "<td>"+ t._json["created_at"] +"</td>"
                "<td>"+ str(t._json["retweet_count"]) +"</td>"
        "</tr>")
        i +=1
    if (i == 1):
        return_html += "<td colspan='7'>No result !</td>"
    return_html += "</tboby></table>"
    return return_html
