#!/usr/bin/python3

import requests
import sys

def fetch_todo_list(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch user information
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Fetch TODO list for the user
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    return user_data, todos_data

def display_todo_progress(employee_id):
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    user_data, todos_data = fetch_todo_list(employee_id)

    if not user_data:
        print(f"Error: Employee with ID {employee_id} not found.")
        sys.exit(1)

    employee_name = user_data.get("name")
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task["completed"]]

    print(f"Employee {employee_name} is done with tasks ({len(done_tasks)}/{total_tasks}):")

    for task in done_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    display_todo_progress(employee_id)

