tasks = []

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

if __name__ == "__main__":
    print("Welcome to my to-do list app:")

    while True:
        print("\n")
        print("-------------------------")
        print("1. Delete a task")
        print("2. Exit")
      
        choice = input("Enter your choice: ")

        # Call the appropriate function based on user choice
        if choice == "1":
            deleteTask()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
