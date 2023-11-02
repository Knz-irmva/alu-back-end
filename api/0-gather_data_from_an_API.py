#!/usr/bin/python3

import requests

def get_employee_todo_list_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Fetch employee name
        response = requests.get(employee_url)
        response.raise_for_status()
        employee_data = response.json()
        employee_name = employee_data["name"]

        # Fetch TODO list for the employee
        response = requests.get(todos_url)
        response.raise_for_status()
        todos_data = response.json()

        # Calculate progress
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for todo in todos_data if todo["completed"])

        # Print progress information
        print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
        print(f"EMPLOYEE_NAME: {employee_name}")
        print(f"NUMBER_OF_DONE_TASKS: {completed_tasks}")
        print(f"TOTAL_NUMBER_OF_TASKS: {total_tasks}")

        # Print the titles of completed tasks
        print("Completed tasks:")
        for todo in todos_data:
            if todo["completed"]:
                print(f"\t{todo['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Error: Invalid data format in the response")

if __name__ == "__main__":
    employee_id = 1  # Replace with the desired employee ID
    get_employee_todo_list_progress(employee_id)
