import json

with open('tasks.json', 'r') as file:
    tasks = json.load(file)

def add_task(task):
    name = input("Enter name of task? ").strip()

if not name:
    print("Name cannot be empty.")
    return
