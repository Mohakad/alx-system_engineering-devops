#!/usr/bin/python3
"""query a list of all hot post"""

import requests


def count_words(subreddit, word_list, after=None, counts={}):
