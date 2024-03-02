class TaskEditing:
    def __init__(self, task_management):
        self.task_management = task_management

    def set_task_status(self, task_id, status):

        task = self.get_task_by_id(task_id)
        if task:
            task.status = status


    def set_prioritization(self, task_id, priority):
        task = self.get_task_by_id(task_id)
        if task:
            task.priority = priority
        pass

    def set_new_date(self,task_id, deadline):
        task = self.get_task_by_id(task_id)
        if task:
            task.deadline = deadline

    def mark_sttus_completed(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            task.status = "Completed"

    def get_task_by_id(self, task_id):
        for task in self.task_management.task_list:
            if task.task_id == task_id:
                return task
        print(f"Task {task_id}")
        
         