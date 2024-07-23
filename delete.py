tasks = []

# Function to delete tasks from the list
def deleteTask():
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


    
    # Call deleteTask() directly
    deleteTask()
