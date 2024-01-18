#!/usr/bin/python3
"""Function to query Reddit API"""
import requests
import sys

def top_ten(subreddit):
    """Return the titles of the top 10 posts from a given subreddit."""

    my_url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    headers = {
        "User-Agent": "linux:0x16advancedapi:v1.0.0 (by /u/Mumin_8)"
    }

    try:
        resp = requests.get(my_url, headers=headers, allow_redirects=False)
        resp.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
    except requests.exceptions.HTTPError as err:
        print(f"Error: {err}")
        return
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
        return

    try:
        some_Obj = resp.json()
        # Check if the response contains JSON data
        if 'data' not in some_Obj:
            print(f"OK")
            return

        results = some_Obj['data'].get('children', [])
        for result in results:
            print(result['data']['title'])
    except requests.exceptions.JSONDecodeError as err:
        print("None")