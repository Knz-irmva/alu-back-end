#!/usr/bin/python3

```python
import requests
import sys

def get_todo_list_progress(employee_id):
user_resp = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
todos_resp = requests.get(f'https
