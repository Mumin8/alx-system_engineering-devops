#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""
import json
import requests


def number_of_subscribers(subreddit):
    """get request to obtain subscribers"""
    headers = {'User-Agent': 'linux:com.myapp:v.1'}
    response = requests.get('https://www.reddit.com/r/{}/about'.
                            format(subreddit), headers=headers)

    if response.status_code == 404:
                return 0

    n_response = requests.get('https://www.reddit.com/r/{}/about.json'.
                              format(subreddit), headers=headers).json()

    return n_response.get('data').get('subscribers')