import json

tasks = []
deleted_tasks = []

def load_tasks_from_file(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data.get("tasks", []), data.get("deleted_tasks", [])
    except FileNotFoundError:
        return [], []

def save_tasks_to_file(filename):
    data = {
        "tasks": tasks,
        "deleted_tasks": deleted_tasks
    }
    with open(filename, "w") as file:
        json.dump(data, file)

def add_task(task_name):

    global sequence_number

    if deleted_tasks:
        deleted_tasks_number = deleted_tasks.pop(0)
    else:
        deleted_task_number = f"d{len(deleted_tasks) + 1}"
    
    task = {
        "sequence_number": deleted_task_number,
        "task_name": task_name,
        "status": "Pending"
    }
    tasks.append(task)
    print(f"Task '{task_name}' added successfully with sequence number {sequence_number}.")
    save_tasks_to_file("tasks.json")

def complete_task(sequence_number):

    for task in tasks:
        if task.get("sequence_number") == sequence_number:
            task["status"] = "Completed"
            print(f"Task '{task.get('task_name')}' marked as completed.")
            save_tasks_to_file("tasks.json")
            return
    print("Task not found or already completed.")

def delete_task(sequence_number):
    for task in tasks:
        if task.get("sequence_number") == sequence_number:
            confirmation = input(f"Are you sure you want to delete task '{task['task_name']}'? (yes/no): ")
            if confirmation.lower() == 'yes':
                task["status"] = "Deleted"
                # Assign a new deleted task number
                deleted_task_number = f"d{len(deleted_tasks) + 1}"
                deleted_tasks.append(deleted_task_number)
                print(f"Task '{task['task_name']}' deleted successfully.")
                save_tasks_to_file("tasks.json")
            else:
                print("Deletion canceled.")
            return
    print("Task not found.")

def list_completed_tasks():

    completed_tasks = [task for task in tasks if task.get("status") == "Completed"]
    if completed_tasks:
        print("Completed Tasks:")
        for task in completed_tasks:
            print(f"{task['sequence_number']}. {task['task_name']} - {task['status']}")
    else:
        print("No completed tasks.")

def list_all_tasks():
    print("All Tasks:")
    for task in tasks:
        if all(key in task for key in ["sequence_number", "task_name", "status"]):
            print(f"{task['sequence_number']}. {task['task_name']} - {task['status']}")
        else:
            print("Invalid task structure found.")

def exit_program():
    print("Exiting program.")
    exit()

# Load tasks from file at the beginning    
tasks, deleted_tasks = load_tasks_from_file("tasks.json")

# main program loop
while True:
    print("\nTask Manager Application")
    print("1. Add a new task")
    print("2. Complete a task")
    print("3. Delete a task")
    print("4. List completed tasks")
    print("5. List all tasks with their statuses")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task_name = input("Enter the task name: ")
        add_task(task_name)
    elif choice == '2':
        sequence_number = int(input("Enter the sequence number of the task to mark as completed: "))
        complete_task(sequence_number)
    elif choice == '3':
        sequence_number = int(input("Enter the sequence number of the task to delete: "))
        delete_task(sequence_number)
    elif choice == '4':
        list_completed_tasks()
    elif choice == '5':
        list_all_tasks()
    elif choice == '6':
        exit_program()
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")