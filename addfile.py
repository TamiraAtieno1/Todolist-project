
tasks = [
]

def add_task(name, due_date):
    """
    Adds a task to the tasks list with the due date 
    """
    tasks.append({"name": name, "due_date": due_date, "completed": False})

def view_tasks():
    """
    Displays all tasks in the tasks list.
    """
    if not tasks:
        print("No tasks to display.")
        return
    for task in tasks:
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"Task: {task['name']}, Due Date: {task['due_date']}, Status: {status}")



