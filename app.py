#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Albin TCHOPBA"
__copyright__ = "Copyright 2020 Albin TCHOPBA and contributors"
__credits__ = ["Albin TCHOPBA and contributors"]
__license__ = "GPL"
__version__ = "3"
__maintainer__ = "Albin TCHOPBA"
__email__ = "Albin TCHOPBA <atchopba @ gmail dot com"
__status__ = "Production"


from flask import Flask, render_template, request, make_response

from treatment import usertweets

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/search", methods=["POST"])
def search():
    search_text = request.form["q"]
    resp = make_response(usertweets.search_tweets(search_text))
    resp.status_code = 200
    resp.headers["Access-Control-ALlow-Origin"] = "*"    
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
