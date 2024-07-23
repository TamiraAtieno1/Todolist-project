#saving tasks
def save_tasks(tasks, filename): #takes the arguments tasks and filename
    try:
        with open(filename, 'w') as file:  #opens the file in write mode
            for task in tasks:
                file.write(f"{task['name']}, {task['due_date']}\n")   #writes the task in the file
    except IOError as e:
        print(f"Error: Unable to write to the file '{filename}' -{e}")  #handles any IOErrors during operations

tasks = [
    {'name':'Complete assignment', 'due_date': '2024-07-25'}  #example task
]
save_tasks(tasks, 'todo_list.txt')   #sets the location where tasks are saved

#loading tasks
def load_tasks(filename): #loads tasks from a file
    tasks = []  #creates an empty list for storing tasks
    try:
        with open(filename, 'r') as file:  #opens files in read mode
            for line in file:  #reads each line inside the file
                parts = line.strip().split(',')
                if len(parts) == 2: #checks if there are 2 parts
                    task = {'name': parts[0], 'due_date': parts[1]} #creates a dictionary for the tasks 
                    tasks.append(task)  #adds a task into the list
    except FileNotFoundError:
        print(f"Error: Unable to retrieve the file'{filename}'")  #handles FileNotFoundError
    except IOError as e:
        print(f"Error: Unable to read from the file '{filename}' -{e}")  #handles any IOError
              
        tasks = []   #sets the task in an empty list
    return tasks     #returns the list of tasks

loaded_tasks = load_tasks('todo_list.txt') #calls the load_tasks function with the file name
for task in loaded_tasks:
    print(f"Task: {task['name']}, Due Date: {task['due_date']}")  #prints the task name and due date