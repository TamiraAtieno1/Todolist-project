# Function to display the list of tasks
tasks=[]

def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")