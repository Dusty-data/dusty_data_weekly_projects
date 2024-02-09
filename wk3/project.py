# Task Manager Application

# Project Description: In this assignment, I will create a task manager application. This application allows users 
# to add, complete, delete, and list their tasks.

# Requirements:
# 1- Tasks will be stored in a Python list, and each task will be represented as a dictionary. Each task should have the following properties:
#    - Sequence Number (Automatically assigned)
#    - Task Name
#    - Status (Completed, Pending, or Deleted)

# 2- Operations that the user can perform:
#    - Add a new task
#    - Complete a task
#    - Delete a task
#    - List completed tasks
#    - List all tasks with their statuses
#    - Exit

# 3- Tasks should automatically receive a sequence number based on the order of addition.

# 4- Newly added tasks should be saved in place of deleted task numbers.

# 5- Tasks should be sorted by sequence number when listed.

# 6- Appropriate feedback should be given to the user after each operation. For example, when adding a new task, the user should see a message indicating that the task has been added.

import json

tasks = []
sequence_number = 1
filename = "tasks.json"

def load_tasks():
    global tasks, sequence_number
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            tasks = data.get("tasks", [])
            sequence_number = data.get("sequence_number", 1)
    except FileNotFoundError:
        pass

def save_tasks():
    data = {"tasks": tasks, "sequence_number": sequence_number}
    with open(filename, "w") as file:
        json.dump(data, file)

def add_task(task_name):
    global sequence_number
    task = {"Sequence Number": sequence_number, "Task Name": task_name, "Status": "Pending"}
    tasks.append(task)
    print(f"Task '{task_name}' has been added with sequence number {sequence_number}.")
    sequence_number += 1
    save_tasks()

def complete_task(sequence_number):
    if not tasks:
        print("No tasks available to complete.")
        return

    task_found = False
    for task in tasks:
        if task["Sequence Number"] == sequence_number:
            task["Status"] = "Completed"
            print(f"Task '{task['Task Name']}' has been marked as completed.")
            task_found = True
            break

    if not task_found:
        print("Task not found.")

def delete_task(sequence_number):
    if not tasks:
        print("No tasks available to delete.")
        return

    task_found = False
    for task in tasks:
        if task["Sequence Number"] == sequence_number:
            task["Status"] = "Deleted"
            print(f"Task '{task['Task Name']}' has been deleted.")
            task_found = True
            break

    if not task_found:
        print("Task not found.")

def list_completed_tasks():
    if not tasks:
        print("No tasks available.")
        return

    completed_tasks = [task for task in tasks if task.get("Status") == "Completed"]
    if not completed_tasks:
        print("No completed tasks.")
    else:
        print("Completed Tasks:")
        for task in completed_tasks:
            print(f"{task.get('Sequence Number', 'N/A')}: {task.get('Task Name', 'N/A')}")



def list_all_tasks():
    if not tasks:
        print("There are no tasks now.")
        return

    print("All Tasks:")
    for task in tasks:
        print(f"{task.get('Sequence Number', 'N/A')}: {task.get('Task Name', 'N/A')} - {task.get('Status', 'N/A')}")



def exit_application():
    print("Exiting Task Manager.")
    save_tasks()
    exit()

def main():
    load_tasks()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Delete Task")
        print("4. List Completed Tasks")
        print("5. List All Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            add_task(task_name)
        elif choice == "2":
            sequence_number = int(input("Enter sequence number of task to complete: "))
            complete_task(sequence_number)
        elif choice == "3":
            sequence_number = int(input("Enter sequence number of task to delete: "))
            delete_task(sequence_number)
        elif choice == "4":
            list_completed_tasks()
        elif choice == "5":
            list_all_tasks()
        elif choice == "6":
            exit_application()
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
