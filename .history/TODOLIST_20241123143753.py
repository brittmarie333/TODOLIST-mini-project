allTasks = []              

def addTask():
    new_task = input("add task: ")
    allTasks.append(new_task)
    print(new_task + " has been added", +  (allTasks), end="")

def viewTasks():
    for i in allTasks:
        print("Your list contains: " + str(allTasks), end="")

def markComplete():
    pass

def deleteTask():
    pass

def quitTask():
    pass

def incomplete():
    quit


    print("***Welcome to the To-Do List App!***\n"
        "Menu:\n"
        "1. Add a task\n"
        "2. View tasks\n"
        "3. Mark a task as complete\n"
        "4. Delete a task\n"
        "5. Quit\n")



try:
    selection = input("Please make your selection: ")
    if selection == "1":
        addTask()
    elif selection == "2":
        viewTasks()
    elif selection == "3":
        markComplete()
    elif selection == "4":
        deleteTask()
    elif selection == "5":
        quit
    else:
        incomplete()
except ValueError:
    print("Incomplete")                                                                                                                                                                                                                                                           