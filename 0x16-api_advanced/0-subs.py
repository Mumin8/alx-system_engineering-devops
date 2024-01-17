#!/usr/bin/python3
"""Function to query reddit api"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    if subreddit is None:
        return None
    my_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16advancedapi:v1.0.0 (by /u/Mumin_8)"
    }
    resp = requests.get(my_url, headers=headers, allow_redirects=False)
    if resp.status_code == 404:
        return 0
    results = resp.json().get("data")
    return results.get("subscribers")
