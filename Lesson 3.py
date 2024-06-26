# Print a welcome message
print("Welcome to the Simple To-Do List!")

#Create an empty list to store tasks
tasks = []
    
# Main loop for the to-do list program
while True:
  
  #Prompt the user to choose an action
  action= input("Enter 'a' to add a task, 'v' to view tasks, 'r' to remove a task, 'c' to mark a task as complete, 'q to quit")
  
  #Add a task
  if action== 'a':
    task= input("Enter a task: ")
    tasks.append({"task": task, "complete": False})
    print("Task added successfully")
    
  #View a task
  elif action == 'v':
    if tasks:
      print("Tasks: ")
      #Loop over tasks to display them
      for i in range(len(tasks)):#for every i (index) within the len (length) of the task list
        print(f"{i + 1}. [{ 'x' if tasks[i]['complete'] else ' ' }] {tasks[i]['task']}")
    else:
      print("No tasks in the list")
      
  #Remove a task
  elif action == 'r':
    if tasks:
      index = int(input("Enter the index you want to remove: ")) -1
      if 0 <= index <=len(tasks):
        del tasks[index]
        print("Item removed")
      else:
        print("Incorrect index")
    else:
      print ("No tasks in the list")
      
  #Marking a task as complete
  elif action =='c':
    if tasks:
      index = int(input("Enter the index you want to mark as complete")) -1
      if 0<=index<=len(tasks):
        tasks[index]['complete'] = True
        print ("Task marked as complete")
      else:
        print("Incorrect index")
    else:
      print("No tasks in the list")
  
  
  #Quit the program  
  elif action == 'q':
    print("Exiting program, goodbye!")
    break

  #Error handling incorrect inputs
  else:
    print("Incorrect input, try again")
