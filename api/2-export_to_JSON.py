#!/usr/bin/python3
"""Export an employee's TODO list to a JSON file."""

import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(
        "{}/users/{}".format(url, employee_id)
    )

    todos_response = requests.get(
        "{}/todos".format(url),
        params={"userId": employee_id}
    )

    user = user_response.json()
    todos = todos_response.json()

    username = user.get("username")

    tasks = []

    for task in todos:
        task_data = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }

        tasks.append(task_data)

    data = {
        employee_id: tasks
    }

    filename = "{}.json".format(employee_id)

    with open(filename, mode="w") as json_file:
        json.dump(data, json_file)
