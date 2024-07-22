tasks = []

# Function to list tasks
def listTasks():
    # Check if there are tasks in the list
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
        # Checks if the task number exists
        if 0 <= taskToDelete < len(tasks):
            # Removes tasks from the list
            deleted_task = tasks.pop(taskToDelete)
            print(f"Task '{deleted_task}' has been deleted.")
        else:
            print(f"Task {taskToDelete + 1} does not exist.")
    # Error handling
    except ValueError:
        print("Invalid input. Please enter a number.")
    except IndexError:
        print("Task index out of range.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to my to-do list app:")
    
    # Call deleteTask() directly
    deleteTask()
