# Task CLI

A simple command-line task manager built with **Python** and **JSON**.

## Features

* Add new tasks
* Update existing tasks
* Delete tasks
* View tasks by status
* Mark tasks as **Not Started**, **In Progress**, or **Completed**
* Store tasks locally using a JSON file
* Clear the console
* Simple command-line interface

## Technologies

* **Python**
* **JSON**
* **File I/O**

## Usage

Run the program:

```bash
python main.py
```

Available commands:

```text
task-cli help
task-cli add <task>
task-cli update <id> <new task>
task-cli delete <id>
task-cli view <All/Not Started/In Progress/Completed>
task-cli mark <id> <status>
clear
break
```

### Examples

Add a task:

```text
task-cli add Learn Python
```

Update a task:

```text
task-cli update 1 Learn Python OOP
```

Delete a task:

```text
task-cli delete 1
```

View all tasks:

```text
task-cli view All
```

Mark a task as completed:

```text
task-cli mark 1 Completed
```

## Data Storage

Tasks are stored in `tasks.json` using the following structure:

```json
{
    "id": 1,
    "task": "Learn Python",
    "status": "Not Started"
}
```

## Project Structure

```text
task-cli/
├── main.py
├── tasks.json
└── README.md
```

## Purpose

This project was created to practice **Python fundamentals, file handling, JSON data management, command-line interfaces, and CRUD operations**.
