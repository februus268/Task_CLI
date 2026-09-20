import json
def getNextId():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

        if not tasks:
            return 1

        return max(task["id"] for task in tasks) + 1

    except FileNotFoundError:
        return 1
def addTask(temp, id, status):
    parts = temp.split()
    task = " ".join(parts[2:])
    task_dict = {"id": id, "task": task, "status": status}
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    tasks.append(task_dict)
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
def updateTask(temp):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("No tasks found.")
        return
    parts = temp.split()
    get_id = int(parts[2])
    new_task = " ".join(parts[3:])
    for task in tasks:
        if (get_id == task['id']):
            saved = task['task']
            task['task'] = new_task
            with open("tasks.json", "w") as file:
                json.dump(tasks, file, indent=4)
            print(f"Task '{saved}' updated to '{new_task}' successfully.")
            break
    else:
        print("Task not found.")
        return

def deleteTask(temp):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("No tasks found.")
        return
    parts = temp.split()
    get_id = int(parts[2])
    for task in tasks:
        if (get_id == task['id']):
            tasks.remove(task)
            with open("tasks.json", "w") as file:
                json.dump(tasks, file, indent=4)
            print(f"Task '{task['task']}' deleted successfully.")
            break
    else:
        print("Task not found.")
def viewTask(temp):
    parts = temp.split()
    needs = parts[2]
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("No tasks found.")
        return
    if not tasks:
        print("No tasks found.")
        return
    if (needs == "all"):
        for task in tasks:
            print(f"ID: {task['id']}, Task: {task['task']}, Status: {task['status']}")
    elif (needs == "not started"):
        for task in tasks:
            if (task['status'] == "not started"):
                print(f"ID: {task['id']}, Task: {task['task']}, Status: {task['status']}")
    elif (needs == "in progress"):
        for task in tasks:
            if (task['status'] == "in progress"):
                print(f"ID: {task['id']}, Task: {task['task']}, Status: {task['status']}")
    elif (needs == "completed"):
        for task in tasks:
            if (task['status'] == "completed"):
                print(f"ID: {task['id']}, Task: {task['task']}, Status: {task['status']}")
def markTask(temp):
    parts = temp.split()
    get_id = int(parts[2])
    new_status = parts[3]
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("No tasks found.")
        return
    for task in tasks:
        if (get_id == task['id']):
            with open("tasks.json", "w") as file:
                task['status'] = new_status
                json.dump(tasks, file, indent=4)
            print(f"Task '{task['task']}' marked as {new_status}.")
            break
    else:
        print("Task not found.")
print("Welcome to task-cli! Type 'task-cli help' for a list of commands.")
idTask = getNextId()
while True:
    user = input("Task-cli> ").lower()
    if (user == "task-cli help"):
        print("task-cli add + Add a new task")
        print("task-cli update + ID task + Update an existing task")
        print("task-cli delete + ID task")
        print("task-cli view - All/Not Started/In Progress/Completed")
        print("task-cli mark + ID + Status (Mark a task as Not Started/In Progress/Completed)")
        print("break - Exit the program")
        print("clear - Clear the console")
    elif (user.startswith("task-cli add ")):
        idTask += 1
        addTask(user, idTask, "Not Started")
    elif (user.startswith("task-cli update ")):
        updateTask(user)
    elif (user.startswith("task-cli delete ")):
        deleteTask(user)
    elif (user.startswith("task-cli view ")):
        viewTask(user)
    elif (user.startswith("task-cli mark ")):
        markTask(user)
    elif (user == "break"):
        print("Exiting the program. Goodbye!")
        break
    elif (user == "clear"):
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
