"""
This module helps you create new tasks, delete, view, and mark it as done.
"""
import json


HLP = """
Enter 1 to create a new task
Enter 2 to delete a task
Enter 3 to view current tasks
Enter 4 to get help (as I said before)
Enter 5 to mark a current task as done
Enter 6 to shutdown the app
"""


def is_new():
    """
    Check if the user is new to the app.

    - If `file.txt` exists and contains 'O', the app continues to the command loop.
    - If the file doesn't exist, it is created and marked as 'O', then the welcome message is shown.
    """
    try:
        with open('file.txt', 'r', encoding='utf-8') as file:
            if file.read().strip() == 'O':
                get_command()
            else:
                welcome_new_users()
    except FileNotFoundError:
        with open('file.txt', 'w', encoding='utf-8') as file:
            file.write('O')
        welcome_new_users()



def read_json():
    """
    Read and return all tasks from 'tasks.json'.

    Returns:
        dict: A dictionary of tasks if the file exists, otherwise an empty dictionary.
    """
    try:
        with open('tasks.json', 'r', encoding='utf-8') as file:
            content = file.read()
            return json.loads(content)
    except FileNotFoundError:
        return {}


def write_json(data):
    """
    Write the given tasks dictionary to 'tasks.json'.

    Args:
        data (dict): The tasks to save, where each key is a task name and each value is a dict
                     with description and is_done status.
    """
    with open('tasks.json', 'w', encoding='utf-8') as file:
        content = json.dumps(data, indent=4)
        file.write(content)


def welcome_new_users():
    """
    Print a welcome message and show help instructions for new users.
    Then start the command input loop.
    """
    print("This is my advanced to-do app, made for you to enter your tasks")
    print("and to not forget them ;)")
    print(HLP)
    print("Would you like to get help in the app? Just enter 'help' and we'll help")
    get_command()


def get_command():
    """
    Continuously prompt the user for a command.

    - Valid commands are integers from 1 to 6.
    - If '6' is entered, the app exits.
    - Otherwise, the command is passed to check_command().
    - Invalid input will re-prompt the user.
    """
    while True:
        command = input("> ")
        if command.isdigit() and 1 <= int(command) <= 6:
            if int(command) == 6:
                return
            check_command(int(command))
        else:
            print("Enter a digit from 1 to 6 please.")
            print("Your input isn't in that range.")



def check_command(command):
    """
    Route the user command to the appropriate function.

    Args:
        command (int): The user-selected command (1–5).
    """
    if command == 1:
        create_new()
    elif command == 2:
        delete()
    elif command == 3:
        view()
    elif command == 4:
        print(HLP)
    elif command == 5:
        mark_done()


def create_new():
    """
    Create a new task and save it to 'tasks.json'.

    - Prompts the user for a task name and optional description.
    - If the name already exists, the user is asked to choose another.
    - The new task is stored with a default 'is_done = False'.
    """
    name = input("Enter the name of the new task you want to make (enter 0 to cancel): ")
    if name == '0':
        return
    data = read_json()
    lower_keys = {k.lower(): v for k, v in data.items()}
    if name.lower() in lower_keys:
        while True:
            print("This name already exists. Try another one.")
            name = input("> ")
            if name.lower() not in lower_keys:
                break
    description = input(
        "Does it have any description?"
        "(0 if it doesn't, else the description) "
    )
    if description == '0':
        description = 'none'
    data[name] = {'description': description, 'is_done': False}
    write_json(data)
    print("New task created successfully. You can use command 3 to see it.")


def delete():
    """
    Delete an existing task from 'tasks.json'.

    - Prompts the user for the task name.
    - If found, asks for confirmation before deletion.
    - If not found, informs the user and re-prompts.
    """
    data = read_json()
    while True:
        inp = input("Enter the name of the task you want to delete: ")
        for name in data.keys():
            if inp.lower() == name.lower():
                confirmation = input(f"Are you sure you want to delete the task named {name}?(y/n)")
                if confirmation == 'y':
                    data.pop(name)
                    write_json(data)
                    print("Deleted successfully.")
                    return
        print("Your entered name doesn't exist.")
        confirmation = input("Would you like to try another name? y/n")
        if confirmation == 'n':
            break


def view():
    """
    View all tasks currently stored in 'tasks.json'.

    - If no tasks exist, displays a message.
    - Otherwise, prints each task's name, description, and completion status.
    """
    count = 1
    data = read_json()
    if data == {}:
        print("There is no task yet.")
    else:
        for task, info in data.items():
            print(f"{count}. Name: {task}")
            print(f"Description: {info['description']}")
            if info['is_done']:
                print("Status: Done")
            else:
                print("Status: Not done")
            count += 1


def mark_done():
    """
    Mark a task as done.

    - Prompts the user for the task name.
    - If the task exists, sets 'is_done = True' and saves changes.
    - If not found, informs the user and asks them if they'd like to try again.
    """
    data = read_json()
    print("The list of current tasks:")
    view()
    while True:
        inp = input("Enter the name of the task you want to mark as done: ")
        for name in data.keys():
            if name.lower() == inp.lower():
                data[name]['is_done'] = True
                write_json(data)
                print("The task is marked as done successfully.")
                return
        print("Task not found.")
        confirmation = input("Would you like to try another name? y/n")
        if confirmation == 'n':
            break


if __name__ == "__main__":
    is_new()
