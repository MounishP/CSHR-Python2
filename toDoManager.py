"""
ToDo list manager
1. display all our task
2. add a new task
3. view all the task
4. exit
"""

tasks = ["wake up", "python class", "get ready", "go to office"]
print("Welcome to the ToDo list manager")

while True:
    if tasks:
        print("Current tasks: ")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

    user_input = input("Options: add / view / exit: ")
    # exit
    if user_input.lower() == "exit":
        print("Exiting the To-Do list Manager. Goodbye!")
        break
    # add
    elif user_input.lower() == "add":
        new_task = input("Enter the task to add: ")
        tasks.append(new_task)  # this will add the newTask to the tasks list
        print(f"Task {new_task} added")
    # view
    elif user_input.lower() == "view":
        if tasks:
            print("Current tasks: ")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No tasks available. Add some tasks first!")
    else:
        print("Invalid option/Null. Please choose correctly")
