#!/usr/bin/python3
"""returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """n of sub"""
    url = "https://www.reddit.com/dev/api/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'subreddit_subscriber_counter/0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    data = response.json()
    subscribers = data['data']['subscribers']
    return subscribers
