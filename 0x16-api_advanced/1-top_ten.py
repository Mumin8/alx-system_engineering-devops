#!/usr/bin/python3
"""Function to query Reddit API"""
import requests
import json

def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts in a subreddit."""
    if not subreddit:
        print(None)
        return

    my_url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {
        "User-Agent": "linux:0x16advancedapi:v1.0.0 (by /u/Mumin_8)"
    }

    try:
        resp = requests.get(my_url, headers=headers, allow_redirects=False)
        resp.raise_for_status()  # Raise an error for bad responses (e.g., 404)
        data = resp.json().get("data", {}).get("children", [])
        for post in data:
            print(post['data']['title'])
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        print(None)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
