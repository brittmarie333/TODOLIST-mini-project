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

print("what would you like to do?" 
    "1. View List, 2. Add item, 3. Remove item, ")

selection  = input("")
                   
if selection == "1":
    viewList()
elif selection == "2":
    addItem()
elif selection == "3":
    removeItem()
else:
    print("Invalid selection")







print("***Welcome to the To-Do List App!***\n"
        "Menu:\n"
        "1. Add a task\n"
        "2. View tasks\n"
        "3. Mark a task as complete\n"
        "4. Delete a task\n"
        "5. Quit\n")