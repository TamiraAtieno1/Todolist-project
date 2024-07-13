def addTask():
  task = input("Please enter a task: ")
  task.append(task)
  print(f"Task '{task}' added to the list.")

def listTasks():
  if not tasks:
    print("All Tasks have been completed,No tasks Available.")
