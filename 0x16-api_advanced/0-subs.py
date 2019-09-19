#!/usr/bin/python3
"""returns the number of subscribers for a given subreddit"""
import json
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers to a subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    r = requests.get(url,
                     headers={'User-Agent': 'uniquestring_dncisghq'},
                     allow_redirects=False)
    if r.status_code == 404:
        return 0
    data = r.json().get("data")
    return data.get("subscribers")
