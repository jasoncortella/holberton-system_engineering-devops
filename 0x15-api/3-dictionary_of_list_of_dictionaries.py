#!/usr/bin/python3
"""Exports TODO list progress info for a given employee ID to JSON"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get("{}users".format(url)).json()
    with open("todo_all_employees.json", "w", newline="") as jsonfile:
        xx = {}
        for user in users:
            uid = user.get('id')
            todos = requests.get("{}todos".format(url),
                                 params={"userId": uid}).json()
            x = {uid: [
                {'username': user.get('username'),
                 'completed': task.get('completed'),
                 'task': task.get('title')}
                for task in todos]}
            xx.update(x)
        json.dump(xx, jsonfile)
