#!/usr/bin/python3
import csv
import requests
import sys


if __name__ == "__main__":
    tasks_status = []
    tasks_title = []
    user = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    request_tasks = requests.get(url + "todos/?userid={}".format(user)).json()
    request_user = requests.get(url + "users/{}".format(user)).json()

    username = request_user["username"]
    name = request_user["name"]

    for task in request_tasks:
        if task["userId"] == int(user):
            tasks_status.append(task["completed"])
            tasks_title.append(task["title"])

    with open(user + ".csv", mode='w', encoding='utf-8') as csv_file:
        fieldnames = ["userId", "name", "completed", "title"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for i in range(len(tasks_status)):
            writer.writerow({"userId": user, "name": username, "completed":
                            tasks_status[i], "title": tasks_title[i]})
