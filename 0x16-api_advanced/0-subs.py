#!/usr/bin/python3
"""returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """n of sub"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'subreddit_subscriber_counter/0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get('data', {}).get('subscribers', 0)
    else:
        return 0
