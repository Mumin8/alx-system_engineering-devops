#!/usr/bin/python3
"""Function to query reddit api"""
import requests

def top_ten(subreddit):
    """Print the titles of the top 10 hot posts on a given subreddit."""
    
    if not subreddit:
        print(None)
        return

    my_url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    headers = {
        "User-Agent": "linux:0x16advancedapi:v1.0.0 (by /u/Mumin_8)"
    }
   
    resp = requests.get(my_url, headers=headers, allow_redirects=False)

    if resp.status_code != 200:
        print(None)
        return
    
    try:
        results = resp.json().get("data", {}).get("children", [])
        for result in results:
            print(result['data']['title'])
    except ValueError as e:
        print(f"Error decoding JSON: {e}")
