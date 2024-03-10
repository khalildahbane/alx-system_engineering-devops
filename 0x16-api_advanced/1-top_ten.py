#!/usr/bin/python3
"""
Use ReditAPI
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit. If not a valid subreddit, print None.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    head = {"User-Agent": "aarizat"}
    r = requests.get(url, headers=head, allow_redirects=False)
    if r.status_code == 404:
        print(None)
        return
    for d in r.json().get("data").get("children"):
        print(d.get("data").get("title"))
