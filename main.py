import json

with open('tasks.json', 'r') as file:
    tasks = json.load(file)

def show_tasks(tasks):
    for task in tasks:
        print(f"Name: {task['name']}, Completed: {task['completed']}")

def find_task(tasks, name):
    for task in tasks:
        if task["name"].lower() == name.lower():
            return task
    return None

def find_and_display_task(tasks):
    name = input("Enter name of task? ")
    
    if not name:
        print("Name cannot be empty.")
        return

    task = find_task(tasks, name)

    if task:
        print(task)

    else:
        print("Task not found.")
       
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
    print("Task added successfully. ")

def mark_task_completed(tasks):
    name = input("Enter name of task? ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    task = find_task(tasks, name)

    if task:
        task["completed"] = True
        save_tasks(tasks)
        print("Task completed.")
    else:
        print("Task doesn't exist.")


def remove_task(tasks):
    name = input("Enter name of task? ").strip()
    
    if not name:
        print("Name cannot be empty.")
        return
    
    task = find_task(tasks, name)

    if task:
        tasks.remove(task)
        save_tasks(tasks)
        print("Task removed.")
    else:
        print("Task not found.")

def menu(tasks):
    choice = ""
    while choice != "6":
        print("\nTask Manager")
        print("1. Show tasks")
        print("2. Find task")
        print("3. Add task")
        print("4. Mark task as completed")
        print("5. Remove task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            find_and_display_task(tasks)

        elif choice == "3":
            add_task(tasks)
        
        elif choice == "4":
            mark_task_completed(tasks)

        elif choice == "5":
            remove_task(tasks)

        elif choice == "6":
            print("Exited...")
            
        else:
            print("Invalid choice. Please try again.")

menu(tasks)
