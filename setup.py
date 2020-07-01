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

from io import open
from os import path

from setuptools import setup

path_ = path.abspath(path.dirname(__file__))

long_description = ""

with open(path.join(path_, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="twitter-search",
    version="0.0.1",
    description="Allows you to search on Twitter. The search returns 100 'last' tweets max. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/atchopba/twitter-search",
    author="atchopba",
    author_email="atchopba@gmail.com",
    classifiers=[
        "Development Status :: 0.0.1",
        "Intended Audience :: End Users/Desktop",
        "License :: GPL-3.0 License ",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="search twitter twitter-api tweepy tweepy-api tweepy-library tweets python python3 tweet",
    install_requires=["pytest>=5.4.3"],
    license="GPL-3.0 License",
    
)
