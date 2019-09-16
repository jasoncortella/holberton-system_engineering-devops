#!/usr/bin/python3
"""Exports TODO list progress info for a given employee ID to JSON"""
from sys import argv
import requests
import json

url = "https://jsonplaceholder.typicode.com/"
uid = argv[1]
user = requests.get("{}users/{}".format(url, uid)).json()
todos = requests.get("{}todos".format(url), params={"userId": uid}).json()

if __name__ == "__main__":
    with open("{}.json".format(uid), "w", newline="") as jsonfile:
        x = {uid: [
            {'username': user.get('username'),
             'completed': task.get('completed'),
             'task': task.get('title')}
            for task in todos]}
        json.dump(x, jsonfile)
