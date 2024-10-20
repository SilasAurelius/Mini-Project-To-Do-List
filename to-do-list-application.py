incomplete = []
complete = []

def adding_task():
    add_task = input("Add a task: ").title()
    incomplete.append(add_task)

def delete_task():
    remove_task = input("Input task to remove: ").title()
    try:
        incomplete.remove(remove_task)
    except ValueError:
        print("Task not found in incomplete tasks.")

def view_task():
    if not incomplete and not complete:
        print("No tasks available.")
    else:
        if incomplete:
            print("Incomplete Tasks:")
            for task in incomplete:
                print(f"- {task}")
        else:
            print("No incomplete tasks.")

        if complete:
            print("Completed Tasks:")
            for task in complete:
                print(f"- {task}")
        else:
            print("No completed tasks.")
# I rewrote this a few times. Though my code would iterate over the incomplete and complete lists, it did not account for showing a message of an empty list.

def completed_task():
    task_done = input("Enter the task completed: ").title()
    if task_done in incomplete:
        incomplete.remove(task_done)
        complete.append(task_done)
    else:
        print("Task not found in incomplete tasks.")

while True:
    print("Menu:\n1. Add a task\n2. View tasks\n3. Mark a task as complete\n4. Delete a task\n5. Quit\n")
    
    try:
        user_choice = int(input("Please enter your numeric response: "))
    except ValueError:
        print("Please enter a numeric response such as 1, 2, 3, 4, or 5.")
        continue 

    if user_choice == 1:
        adding_task()
    elif user_choice == 2:
        view_task()
    elif user_choice == 3:
        completed_task()
    elif user_choice == 4:
        delete_task()
    elif user_choice == 5:
        print("Thank you for using the To-Do-List App!\nGoodbye!")
        break
    else:
        print("Please enter a numeric option: ")
