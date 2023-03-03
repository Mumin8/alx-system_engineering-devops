#!/usr/bin/python3w
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests
import praw

# Initialize the Reddit instance with the praw module
reddit = praw.Reddit(client_id='N8YfdZtlSu0aalYtl-SgTg', client_secret='SjuG-hCdJiN4H_LQDBGwDml52chPrw',
        user_agent='Window:trying:1/0(u/Mumin_8)')

def count_words(subreddit, word_list, posts=None, count_dict=None):
    # If it's the first iteration, get the hot posts from the subreddit
    if posts is None:
        try:
            posts = reddit.subreddit(subreddit).hot(limit=100)
        except:
            return
    # If it's the first iteration, initialize the count_dict
    if count_dict is None:
        count_dict = {}
        for word in word_list:
            count_dict[word.lower()] = 0
    # Loop through the posts and count the occurrences of each word in the title
    for post in posts:
        title_words = post.title.lower().split()
        for word in word_list:
            if word.lower() in title_words:
                count_dict[word.lower()] += title_words.count(word.lower())
    # Recursively call the function with the next batch of posts
    if len(list(posts)) == 100:
        count_words(subreddit, word_list, posts=reddit.subreddit(subreddit).hot(limit=100, params={'after': post.name}), count_dict=count_dict)
    else:
        # Sort the dictionary by count (descending) and word (ascending)
        sorted_dict = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        # Print the results
        for word, count in sorted_dict:
            if count > 0:
                print(word, count)
