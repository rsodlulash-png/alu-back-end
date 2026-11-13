#!/usr/bin/python3
"""Export an employee's TODO list to a CSV file."""

import csv
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

    user = user_response.json()
    todos = todos_response.json()

    username = user.get("username")

    filename = "{}.csv".format(employee_id)

    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.writer(
            csv_file,
            quoting=csv.QUOTE_ALL
        )

        writer.writerow([
            "USER_ID",
            "USERNAME",
            "TASK_COMPLETED_STATUS",
            "TASK_TITLE"
        ])

        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
