import json
from unicodedata import name

with open('data.json', 'r') as file:
    data = json.load(file)

def add_task(task):
    name = input("Enter name of task? ").strip()

if not name:
    print("Name cannot be empty.")
    return
