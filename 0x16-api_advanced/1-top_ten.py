#!/usr/bin/python3
""" Module for task 1 """


def top_ten(subreddit):
    import requests

    headers = {
        'User-Agent': 'My-User-Agent'
    }
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code > 300:
        print("None")
        return
    listings = r.json()["data"]["children"]
    for listing in listings:
        print(listing["data"]["title"])