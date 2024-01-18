#!/usr/bin/python3
""" Module for task 100 """
import requests


def get_words(headers, data, subreddit, word_dic={}):
    if data:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
            subreddit, data)
    else:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code > 300:
        return None
    listings = r.json()
    for listing in listings["data"]["children"]:
        words = listing["data"]["title"].split()
        for word in words:
            if word.lower() in word_dic.keys():
                word_dic[word.lower()] += 1
            else:
                word_dic[word.lower()] = 0
    if listings["data"]["after"] is not None:
        return get_words(headers, listings["data"]["after"],
                         subreddit, word_dic)
    else:
        return word_dic


def count_words(subreddit, word_list):
    headers = {
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/76.0.3809.132 Safari/537.36')
    }
    words = get_words(headers, None, subreddit)
    if words is None:
        return None
    for word in word_list:
        if word in words and words.get(word) != 0:
            print("{}: {}".format(word, words[word]))
