#!/usr/bin/python3
"""returns the number of subscribers for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Print all hot posts for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    r = requests.get(url,
                     headers={'User-Agent': 'uniquestring_dncisghq'},
                     params={"after": after,
                             "count": count},
                     allow_redirects=False)
    if r.status_code == 404:
        return None
    data = r.json().get("data")
    after = data.get("after")
    count += data.get("dist")
    for child in data.get("children"):
        hot_list.append(child.get("data").get("title"))
    if after:
        return recurse(subreddit, hot_list, count, after)
    return hot_list
