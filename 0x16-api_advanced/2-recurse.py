#!/usr/bin/python3
"""
Use ReditAPI
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    queries the Reddit API and returns a list containing the titles of all
    hot articles for a given subreddit. If no results are found for the given
    subreddit, the function will return None.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    head = {"User-Agent": "aarizat"}
    params = {"after": after, "count": count}
    r = requests.get(url, headers=head, params=params)
    if r.status_code == 404:
        return
    after = r.json().get("data").get("after")
    count += r.json().get("data").get("dist")
    for _dict in r.json().get("data").get("children"):
        hot_list.append(_dict.get("title"))
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
