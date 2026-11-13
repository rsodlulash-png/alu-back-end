#!/usr/bin/python3
"""Export all employees' TODO lists to a JSON file."""

import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"

    users_response = requests.get("{}/users".format(url))
    users = users_response.json()

    all_employees = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        todos_response = requests.get(
            "{}/todos".format(url),
            params={"userId": user_id}
        )

        todos = todos_response.json()

        tasks = []

        for task in todos:
            task_data = {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }

            tasks.append(task_data)

        all_employees[str(user_id)] = tasks

    filename = "todo_all_employees.json"

    with open(filename, mode="w") as json_file:
        json.dump(all_employees, json_file)
