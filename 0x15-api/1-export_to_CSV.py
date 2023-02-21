#!/usr/bin/python3
"""Exports to-do list information for a given 
    employee ID to CSV format.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    ID = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + 'users/{}'.format(ID)).json()
    user_name = user.get('username')
    todo = requests.get(url + 'todos', auth=('user', 'pass')).json()
    with open('{}.csv'.format(ID), 'w', newline='') as myfile:
         writer = csv.writer(myfile,quoting=csv.QUOTE_ALL)
         [writer.writerow(
            [ID, user_name, t.get("completed"), t.get("title")]
         ) for t in todo]
