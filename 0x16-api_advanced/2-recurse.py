#!/usr/bin/python3
"""Function to query reddit api recursively"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Returns a list of titles of all hot articles  on a given subreddit."""
    if hot_list is None:
        hot_list = []

    my_url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after} if after else {}

    headers = {
        "User-Agent": "linux:0x16advancedapi:v1.0.0 (by /u/Mumin_8)"
    }

    try:
        resp = requests.get(
                my_url, headers=headers,
                params=params, allow_redirects=False
                )
        resp.raise_for_status()
        data = resp.json()['data']
        after = data.get('after')

        for post in data['children']:
            hot_list.append(post['data']['title'])

        if after:
            recurse(subreddit, hot_list, after)

    except requests.exceptions.RequestException as e:
        return None

    return hot_list
