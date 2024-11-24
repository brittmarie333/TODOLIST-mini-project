def viewList():
    for i in shoppingList:
        print("Your list contains: " + str(shoppingList), end="")
              
def addTask():
    new_task = input("add task: ")
    taskList.append(task)
    print((task + " has been added"))

def removeTask():
    pass

taskList = ['clean house', 'grocery shop']  

print("***Welcome to the To-Do List App!***\n"
        "Menu:\n"
        "1. Add a task\n"
        "2. View tasks\n"
        "3. Mark a task as complete\n"
        "4. Delete a task\n"
        "5. Quit\n")

selection  = input("")
                   
if selection == "1":
    addTask()
elif selection == "2":
    viewTasks()
elif selection == "3":
    markComplete()
elif selection == "4":
    
else:
    print("Invalid selection")
