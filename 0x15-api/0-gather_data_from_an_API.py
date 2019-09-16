#!/usr/bin/python3
"""returns TODO list progress info for a given employee ID"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    uid = sys.argv[1]
    user = requests.get("{}users/{}".format(url, uid)).json()
    todos = requests.get("{}todos".format(url), params={"userId": uid}).json()
    done = [task.get("title") for task in todos if task.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))
    [print("\t {}".format(title)) for title in done]
