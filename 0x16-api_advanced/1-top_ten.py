#!/usr/bin/python3
"""
Use ReditAPI
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit. If an
    invalid subreddit is given, the function will return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    head = {"User-Agent": "aarizat"}
    r = requests.get(url, headers=head, allow_redirects=False)
    if r.status_code == 404:
        return 0
    return r.json().get("data").get("subscribers")
