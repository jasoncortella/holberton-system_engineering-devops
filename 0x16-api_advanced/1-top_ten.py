#!/usr/bin/python3
"""returns the number of subscribers for a given subreddit"""
import requests


def top_ten(subreddit):
    """Print the top 10 hot posts for a subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    r = requests.get(url,
                     headers={'User-Agent': 'uniquestring_dncisghq'},
                     allow_redirects=False,
                     params={"limit": 10})
    if r.status_code == 404:
        print("None")
    else:
        data = r.json().get("data").get("children")
        for child in data:
            print(child.get("data").get("title"))
