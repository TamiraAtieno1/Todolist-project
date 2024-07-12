tasks = []

# Function to add tasks
def addTask():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"'{task}' added to the list.")

# Function to mark the completed tasks, doesn't work
def markCompletedTask():
    listTasks()
    try:
        taskToMark = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= taskToMark < len(tasks):
            tasks[taskToMark] = "[completed] " + tasks[taskToMark]
            print(f"Task {taskToMark + 1} has been marked as completed.")
        else:
            print(f"Task {taskToMark + 1} has not been found.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Function to list tasks
def listTasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Function to delete tasks from the list
def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the task number to delete: ")) - 1
        if 0 <= taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete + 1} has been deleted.")
        else:
            print(f"Task {taskToDelete + 1} does not exist.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Function to view all tasks
def viewTasks():
    listTasks()
    input("Press Enter to continue...")
    print("\n")
    print("-------------------------")
    print("Task List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print("-------------------------")
    print("\n")
        
if __name__ == "__main__":
    print("Welcome to my to-do list app:")

    while True:
        print("\n")
        print("-------------------------")
        print("1. Add a task")
        print("2. Mark a task as completed")
        print("3. Delete a task")
        print("4. View all tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        # Call the appropriate function based on user choice
        if choice == "1":
            addTask()
        elif choice == "2":
            markCompletedTask()
        elif choice == "3":
            deleteTask()
        elif choice == "4":
            viewTasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

    print("Goodbye!")
