#!/usr/bin/python3

"""
A script to gather information about an employee's TODO list progress
from a REST API and export it to a CSV file.

Usage: python3 script_name.py <employee_id>

Requirements:
- You must have the requests module installed.
- Replace script_name.py with the actual script filename.
"""

import sys
import requests
import csv

def get_employee_todo_list_progress(employee_id):
    """
    Retrieve and display information about an employee's TODO list progress
    and export it to a CSV file.

    Args:
        employee_id (int): The employee's ID.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Fetch employee data
        response = requests.get(employee_url)
        response.raise_for_status()
        employee_data = response.json()
        employee_name = employee_data.get("name", "Unknown Employee")

        # Fetch TODO list for the employee
        response = requests.get(todos_url)
        response.raise_for_status()
        todos_data = response.json()

        # Create a CSV file for the employee
        csv_filename = f"{employee_id}.csv"
        with open(csv_filename, mode="w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            for todo in todos_data:
                task_title = todo.get("title", "Untitled Task")
                completed_status = "True" if todo.get("completed") else "False"
                csv_writer.writerow([employee_id, employee_name, completed_status, task_title])

        print(f"Data exported to {csv_filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Error: Invalid data format in the response")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_list_progress(employee_id)

