#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import sys
import requests

if __name__ == "__main__":
    all_tasks = 0
    comp_tasks = 0
    todos = requests.get(
            "https://jsonplaceholder.typicode.com/todos", auth=(
            'user', 'pass'))
    users = requests.get(
            "https://jsonplaceholder.typicode.com/users", auth=(
            'user', 'pass'))

    ID = sys.argv[1]

    for user in users.json():
        if ID == str(user["id"]):
            user_name =  user["name"]

    for todo in todos.json():
        if ID == str(todo["userId"]):
            all_tasks += 1
            if todo["completed"]:
                comp_tasks += 1
    print("Employee {} is done with tasks({}/{}):".format(
                    user_name, comp_tasks, all_tasks))
    for complete in todos.json():
        if complete.get("completed") and ID == str(complete["userId"]):
                print("{}".format(complete["title"]))

