# simple task manager application with user authentication and task management features. It allows users to register, log in, add tasks, view tasks, mark tasks as completed, and delete tasks. The user data and tasks are stored in JSON files for persistence.
import json
import hashlib
import os

# Load users from JSON files.
def load_users():
    if os.path.exists("users.json"):
        with open("users.json", "r") as file:
            return json.load(file)
    
    return {}

# Save users to JSON files.
def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

# Load tasks from JSON files.
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    
    return {}

# Save tasks to JSON files.
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

# Hash password using SHA-256.
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# User registration function that checks for existing usernames and saves new users with hashed passwords.
def register_user(users):
    username = input("Enter a username: ")

    if username in users:
        print("Username already exists. Please choose a different one.")
        return None
    
    password = input("Enter a password: ")
    users[username] = hash_password(password)
    save_users(users)
    print("User registered successfully!")
    return username

# User login function that verifies the username and password against the stored hashed passwords.
def login_user(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == hash_password(password):
        print("Login successful!")
        return username
    else:
        print("Invalid username or password.")
        return None
    
# Task management functions that allow users to add, view, complete, and delete tasks. Each task is associated with a user and stored in a JSON file for persistence.
def add_task(tasks, username):
    description = input("Enter task description: ")
    
    if username not in tasks:
        tasks[username] = []

    task_id = len(tasks[username]) + 1
    task = {
        "id": task_id,
        "description": description,
        "status": "Pending"
    }
    tasks[username].append(task)

    save_tasks(tasks)

    print("Task added successfully.")

# View tasks function that displays the tasks associated with the logged-in user, showing the task ID, description, and status.
def view_tasks(tasks, username):

    if username not in tasks or not tasks[username]:
        print("No tasks found.")
        return

    print("\nYour Tasks:")

    for task in tasks[username]:
        print(
            f"ID: {task['id']} | "
            f"Task: {task['description']} | "
            f"Status: {task['status']}"
        )

# Mark task as completed function that allows users to update the status of a task to "Completed" based on the task ID.
def complete_task(tasks, username):

    task_id = int(input("Enter task ID to mark as completed: "))

    for task in tasks.get(username, []):

        if task["id"] == task_id:
            task["status"] = "Completed"
            save_tasks(tasks)
            print("Task marked as completed.")
            return

    print("Task not found.")

# Delete task function that allows users to remove a task from their list based on the task ID.
def delete_task(tasks, username):

    task_id = int(input("Enter task ID to delete: "))

    for task in tasks.get(username, []):

        if task["id"] == task_id:
            tasks[username].remove(task)
            save_tasks(tasks)
            print("Task deleted successfully.")
            return

    print("Task not found.")

# Task menu function that provides a user interface for managing tasks, allowing users to add, view, complete, and delete tasks, as well as log out.
def task_menu(tasks, username):

    while True:
        try:

            print("\nTask Manager")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task Completed")
            print("4. Delete Task")
            print("5. Logout")

            choice = int(input("Enter choice: "))

            if choice == 1:
                add_task(tasks, username)

            elif choice == 2:
                view_tasks(tasks, username)

            elif choice == 3:
                complete_task(tasks, username)

            elif choice == 4:
                delete_task(tasks, username)

            elif choice == 5:
                print("Logging out...")
                break

            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")

# Main function that serves as the entry point of the application, allowing users to register, log in, and access the task management features through a menu-driven interface.
def main():

    users = load_users()
    tasks = load_tasks()


    while True:
        try:
            print("\nWelcome to Task Manager")
            print("1. Register")
            print("2. Login")
            print("3. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                register_user(users)

            elif choice == 2:

                username = login_user(users)

                if username:
                    task_menu(tasks, username)

            elif choice == 3:
                print("Exiting program.")
                break

            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")

main()