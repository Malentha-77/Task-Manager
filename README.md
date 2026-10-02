# Task Manager

A simple command-line task manager built with Python.

## Features

* Show all tasks
* Find a task by name
* Add a new task
* Mark tasks as completed
* Remove tasks
* Validate user input
* Save tasks to JSON
* Load tasks when the program starts

## Technologies

* Python
* JSON

## How It Works

Tasks are stored as dictionaries inside a Python list.

Each task contains:

```python
{
    "name": "Learn Python",
    "completed": False
}
```

The task data is saved in `tasks.json`, allowing changes to remain available when the program is run again.

## Running the Program

Make sure Python is installed, then run:

```bash
python main.py
```

Follow the menu instructions to manage your tasks.

## What I Learned

This project helped me practice:

* Functions
* Lists and dictionaries
* Loops and conditions
* User input and validation
* Boolean values
* Searching through data
* Adding and removing items from lists
* Updating dictionary values
* `try` / `except` concepts
* JSON data
* Reading and writing files
* Connecting multiple functions into a working program
* Building a menu-driven application

## Project Structure

```text
task-manager-python/
├── main.py
├── tasks.json
└── README.md
```
