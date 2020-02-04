#!/usr/bin/python3
"""
Using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
Extension script to export data in JSON format.
"""
if __name__ == "__main__":
    import json
    import requests
    import sys

    employee_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'

    url = base_url + 'users/' + employee_id
    response = requests.get(url)

    # username of the employee
    employee_username = response.json().get('username')

    url = base_url + 'todos'
    response = requests.get(url)

    # "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    tasks = [task for task in response.json()
             if task.get('userId') is int(employee_id)]

    my_list = []
    for task in tasks:
        new_dict = {"task": task['title'],
                    "completed": task['completed'],
                    "username": employee_username}
        my_list.append(new_dict)

    tasks_dictionary = {sys.argv[1]: my_list}
    with open('{}.json'.format(sys.argv[1]), 'w') as f:
        json.dump(tasks_dictionary, f)
