#!/usr/bin/python3
"""Function to query reddit api"""
import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    my_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16advancedapi:v1.0.0 (by /u/Mumin_8)"
    }
    response = requests.get(my_url, headers=headers, allow_redirects=False)
    if response.status_code == 302:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
