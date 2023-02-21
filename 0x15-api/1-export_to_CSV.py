#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    ID = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(ID), "w", newline="") as myfile:
        writer = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [ID, username, t.get("completed"), t.get("title")]
         ) for t in todos]
