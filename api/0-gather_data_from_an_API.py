#!/usr/bin/python3

"""
A script to gather information about an employee's TODO list progress
from a REST API.

Usage: python3 script_name.py <employee_id>

Requirements:
- You must have the requests module installed.
- Replace script_name.py with the actual script filename.
"""

import sys
import requests

def get_employee_todo_list_progress(employee_id):
    """
    Retrieve and display information about an employee's TODO list progress.

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

        # Calculate progress
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for todo in todos_data if todo.get("completed"))

        # Print progress information
        print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
        print(f"{employee_name}: {employee_name}")
        print(f"NUMBER_OF_DONE_TASKS: {completed_tasks}")
        print(f"TOTAL_NUMBER_OF_TASKS: {total_tasks}")

        # Print the titles of completed tasks
        print("Completed tasks:")
        for todo in todos_data:
            if todo.get("completed"):
                print(f"\t{todo.get('title', 'Untitled Task')}")

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

