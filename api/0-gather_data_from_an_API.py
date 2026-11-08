
#!/usr/bin/python3
"""Gather employee TODO list progress from a REST API."""

import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(
        "{}/users/{}".format(url, employee_id)
    )
    todos_response = requests.get(
        "{}/todos".format(url),
        params={"userId": employee_id}
    )

    employee = user_response.json()
    todos = todos_response.json()

    employee_name = employee.get("name")
    completed_tasks = [
        task for task in todos if task.get("completed") is True
    ]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name,
            len(completed_tasks),
            len(todos)
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))

