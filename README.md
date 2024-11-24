
# 1. TODO List Mini Project

In this project I have created a program to manage a todo list. 

#### What functions do I need for my todo list?

*add task*
*view task*
*mark complete*
*delete*
*quit*

#### What are the expectations of this program?

Code must be able to perform the required functions and produce an output supporting the provided selection. 
Try & Except to anticipate known errors.

#### Extensions needed:
python
python debugger
markdown checkboxes
markdown emoji


##### ***Where is the program?*** 
I will provide the link to access my program at the end of this README file.


### Programming steps:
***Part One: Establish greeting and needed tasks!*** 
*Welcome to the To-Do List App!*
        Menu:
        1. Add a task
        2. View tasks
        3. Mark a task as complete
        4. Delete a task
        5. Quit


***Part Two: Python def used to create functions for the selections*** 
```python def used for selections 
def addTask():
    new_task = input("add task: ")
    allTasks.append(new_task)
    print(new_task + " has been added\n", [allTasks], end="")

def viewTasks():
    for i in allTasks:
        print("Your list contains: \n", [allTasks])
        continue

def markComplete():
    completedTask = input("Which task is completed?: ")
    updatedTasks = allTasks.remove(completedTask)
    print("Congratulations, " + completedTask + " has been marked completed! \n Your remaining tasks are ",  updatedTasks)
    

def deleteTask():
    removeTask = input("Which task would you like to delete?: " )
    print("The task has been removed \n", [allTasks], allTasks.remove(removeTask))
    
def quitTask():
    quit

def incomplete():
    quit
```
***Part Three: Requirement is to use try and except block, with finally, for known errors. (value errors) I will use python try and except block with a nested if statement to achieve the best list program***
```python try and except block with nested if statement

try:
    print("***Welcome to the To-Do List App!***\n"
        "Menu:\n"
        "1. Add a task\n"
        "2. View tasks\n"
        "3. Mark a task as complete\n"
        "4. Delete a task\n"
        "5. Quit\n")
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

finally:
    print("Thank you!")

```
#### *Examples of code:*
![image showing the output of selection 1](screenshots/addtask.jpg)

You can find the link to the project here: