class TaskTracking:

    def __init__(self, task_management):
        self.task_management = task_management

    def get_task_status(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            return print(f"Task with ID {task_id}'s status is {task.status}")
        else:
            return print(f"Task with Id {task_id} not found.")
        

    def get_task_deadline(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            return print(f"Task with ID {task_id}'s status is {task.deadline}")
        else:
            return print(f"Task with Id {task_id} not found.")
    
    
    def get_task_color(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            return print(f"Task with ID {task_id}'s status is {task.color}")
        else:
            return print(f"Task with Id {task_id} not found.")