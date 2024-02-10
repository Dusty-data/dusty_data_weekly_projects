tasks = []

def add_task(task_name):
    # Check if there are any deleted tasks and get their sequence numbers
    deleted_indexes = [task['Sequence Number'] for task in tasks if task['Status'] == 'Deleted']
    
    # If there are deleted tasks
    if deleted_indexes:
        # Get the minimum sequence number among deleted tasks
        seq_number = min(deleted_indexes)
        # Find the task with the minimum sequence number
        for task in tasks:
            if task['Sequence Number'] == seq_number:
                # Update task details with new task name and change status to 'Pending'
                task['Task Name'] = task_name
                task['Status'] = 'Pending'
                # Print a message indicating the addition of the task
                print(f"Task '{task_name}' added with sequence number {seq_number}.")
                return
    # If there are no deleted tasks
    else:
        # If there are no tasks in the list, set sequence number to 1
        if len(tasks) == 0:
            seq_number = 1
        # Otherwise, set sequence number to the next number after the last task's sequence number
        else:
            seq_number = tasks[-1]['Sequence Number'] + 1
        # Add the new task with the determined sequence number and 'Pending' status
        tasks.append({'Sequence Number': seq_number, 'Task Name': task_name, 'Status': 'Pending'})
        # Print a message indicating the addition of the task
        print(f"Task '{task_name}' added with sequence number {seq_number}.")


def complete_task(seq_number):
    # Find the task with the given sequence number and not deleted
    task = next((task for task in tasks if task['Sequence Number'] == seq_number and task['Status'] != 'Deleted'), None)
    # If such a task is found
    if task:
        # Update task status to 'Completed'
        task['Status'] = 'Completed'
        # Print a message indicating task completion
        print(f"Task '{task['Task Name']}' marked as completed.")
    else:
        # If no such task is found or it's already completed, print a message
        print("Task not found or already completed.")

def delete_task(seq_number):
    # Find the task with the given sequence number
    task = next((task for task in tasks if task['Sequence Number'] == seq_number), None)
    # If such a task is found
    if task:
        # Update task status to 'Deleted'
        task['Status'] = 'Deleted'
        # Print a message indicating task deletion
        print(f"Task '{task['Task Name']}' deleted.")
    else:
        # If no such task is found, print a message
        print("Task not found.")

def list_completed_tasks():
    # Filter tasks with status 'Completed'
    completed_tasks = [task for task in tasks if task['Status'] == 'Completed']
    # If there are completed tasks
    if completed_tasks:
        # Print the list of completed tasks
        print("Completed Tasks:")
        for task in completed_tasks:
            print(f"Sequence Number: {task['Sequence Number']}, Task Name: {task['Task Name']}")
    else:
        # If there are no completed tasks, print a message
        print("No completed tasks.")

def list_all_tasks():
    # Sort tasks by sequence number
    sorted_tasks = sorted(tasks, key=lambda x: x['Sequence Number'])
    # Print all tasks with their status
    print("All Tasks with Status:")
    for task in sorted_tasks:
        print(f"Sequence Number: {task['Sequence Number']}, Task Name: {task['Task Name']}, Status: {task['Status']}")

def display_menu():
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. Complete Task")
    print("3. Delete Task")
    print("4. List Completed Tasks")
    print("5. List All Tasks")
    print("6. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            task_name = input("Enter task name: ")
            add_task(task_name)
        elif choice == '2':
            seq_number = int(input("Enter sequence number of task to mark as completed: "))
            complete_task(seq_number)
        elif choice == '3':
            seq_number = int(input("Enter sequence number of task to delete: "))
            delete_task(seq_number)
        elif choice == '4':
            list_completed_tasks()
        elif choice == '5':
            list_all_tasks()
        elif choice == '6':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()