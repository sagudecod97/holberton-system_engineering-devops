#!/usr/bin/python3
"""
Using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
Extension script to export data in JSON format.
"""
if __name__ == "__main__":
    import json
    import requests

    base_url = 'https://jsonplaceholder.typicode.com/'

    url = base_url + 'users/'
    users_response = requests.get(url)
    users = users_response.json()

    users_dict = {}
    for current_user in users:
        url = base_url + 'todos'
        response = requests.get(url)

    employee_id = current_user.get('id')
    # print(employee_id)

    # "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    tasks = [task for task in response.json()
             if task.get('userId') is int(employee_id)]

    my_list = []
    for task in tasks:
        new_dict = {"username": current_user['username'],
                    "task": task['title'],
                    "completed": task['completed'],
                    }
        my_list.append(new_dict)
    users_dict[current_user.get('id')] = my_list

    with open('{}.json'.format('todo_all_employees'), 'w') as f:
        json.dump(users_dict, f)
