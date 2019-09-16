#!/usr/bin/python3
"""Exports TODO list progress info for a given employee ID to CSV"""
from sys import argv
import requests
import csv

url = "https://jsonplaceholder.typicode.com/"
uid = argv[1]
user = requests.get("{}users/{}".format(url, uid)).json()
todos = requests.get("{}todos".format(url), params={"userId": uid}).json()

if __name__ == "__main__":
    with open("{}.csv".format(uid), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([uid,
                             user.get('username'),
                             task.get('completed'),
                             task.get('title')])
