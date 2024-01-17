#!/usr/bin/python3
"""Function to query reddit api"""
import requests

def top_ten(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    
    my_url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    headers = {
        "User-Agent": "linux:0x16advancedapi:v1.0.0 (by /u/Mumin_8)"
    }
   
    resp = requests.get(my_url, headers=headers, allow_redirects=False)
    if resp.status_code == 404:
        print(None)
        return
    results = resp.json().get("data")
    results = results.get('children')
    for result in results:
        print(result['data']['title'])