#!/usr/bin/python3
import json
import requests
import sys

if __name__ == "__main__":

    total_tasks = 0
    tasks_completed = 0
    arr_tasks_title = []
    user = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    request_tasks = requests.get(url + "users/{}/todos".format(user)).json()
    request_user = requests.get(url + "users/{}".format(user)).json()

    for task in request_tasks:
        if task["completed"]:
            tasks_completed += 1
            arr_tasks_title.append(task["title"])
        total_tasks += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(request_user["name"], tasks_completed, total_tasks))
    for task in arr_tasks_title:
        print("\t {}".format(task))
