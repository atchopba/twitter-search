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

from flask import Blueprint, request, make_response
from flask import render_template

from .core import usertweets

# Blueprint Configuration
main_bp = Blueprint('main_bp', 
                    __name__,
                    template_folder='templates',
                    static_folder='static')

@main_bp.route("/")
def home():
    return render_template('index.html')


@main_bp.route("/search", methods=["POST"])
def search():
    search_text = request.form["q"]
    resp = make_response(usertweets.search_tweets(search_text))
    resp.status_code = 200
    resp.headers["Access-Control-ALlow-Origin"] = "*"    
    return resp
