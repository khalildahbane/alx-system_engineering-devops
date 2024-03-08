#!/usr/bin/python3
"""
Use ReditAPI
"""
import requests


def number_of_subscribers(subreddit):
"""Queries the Reddit API and returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    head = {"User-Agent": "aarizat"}
    r = requests.get(url, headers=head, allow_redirects=False)
    if r.status_code == 404:
        return 0
    return r.json().get("data").get("subscribers")
