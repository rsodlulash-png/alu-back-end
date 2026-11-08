
#!/usr/bin/python3
"""Retrieve an employee's TODO list progress from an API."""

import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    base_url = "https://jsonplaceholder.typicode.com"

    employee_response = requests.get(
        "{}/users/{}".format(base_url, employee_id)
    )

    todos_response = requests.get(
        "{}/todos".format(base_url),
        params={"userId": employee_id}
    )

    employee = employee_response.json()
    todos = todos_response.json()

    employee_name = employee.get("name")
    total_tasks = len(todos)

    completed_tasks = []

    for task in todos:
        if task.get("completed") is True:
            completed_tasks.append(task)

    number_of_done_tasks = len(completed_tasks)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name,
            number_of_done_tasks,
            total_tasks
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))

