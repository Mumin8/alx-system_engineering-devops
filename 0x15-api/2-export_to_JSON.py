#!/usr/bin/python3
"""Python script to export data in the JSON format"""
import json
import requests
import sys

if __name__ == "__main__":
    ID = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(ID)).json()
    todo = requests.get(url + 'todos', auth=('user', 'pass')).json()
    user_name = user['username']
    value = []
    mydict = {}
    for sub_dict in todo:
        if ID == str(sub_dict.get('userId')):
            comp = sub_dict.get('completed')
            sub_dict['task'] = sub_dict['title']
            del sub_dict['completed']
            del sub_dict['userId']
            del sub_dict['id']
            del sub_dict['title']
            sub_dict['completed'] = comp
            sub_dict['username'] = user_name
            value.append(sub_dict)
    mydict[ID] = value
    with open('{}.json'.format(ID), 'w') as f:
        json.dump(mydict, f)
