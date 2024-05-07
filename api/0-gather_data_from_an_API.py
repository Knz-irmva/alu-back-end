#!/usr/bin/python3

import sys
import requests

def gather_todo_progress(employee_id):
    # Define the base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Retrieve employee information
    employee_info_response = requests.get(f'{base_url}/users/{employee_id}')
    employee_info = employee_info_response.json()
    employee_name = employee_info['name']

    # Retrieve employee's TODO list
    todo_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todo_list = todo_response.json()

    # Calculate progress
    total_tasks = len(todo_list)
    completed_tasks = sum(1 for task in todo_list if task['completed'])

    # Print employee progress
    print(f'Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):')

    # Print titles of completed tasks
    for task in todo_list:
        if task['completed']:
            print(f'\t{task["title"]}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    gather_todo_progress(employee_id)

