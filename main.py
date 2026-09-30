import json

with open('tasks.json', 'r') as file:
    tasks = json.load(file)


def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    name = input("Enter name of task? ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    new_task = {
            "name": name,
            "completed": False
        }

    tasks.append(new_task)
    save_tasks(tasks)
