
from datetime import datetime
from abc import ABC, abstractmethod

class Task(ABC):
    def __init__(Self, task_id, task_name, deadline, status="Pending"):
        self.task_id = task_id
        self.task_name = task_name
        self.deadline = deadline
        self.status = status
        self.priority = "Low"
        self.color_your_task()

    @abstractmethod
    def color_your_task():
        pass

    def days_to_accomplish_task(self):
        current_date = datetime.now().date()
        deadline_date = datetime.strptime(self.deadline, "%Y-%m-%d").date()
        remaining_days = (deadline_date - current_date).days
        return remaining_days
    def __str__(self):
        return f"Task ID: {self.task_id}, Name: {self.task_name}, Deadline: {self.deadline}, Color: {self.color}, status: {self.status}, Priority: {self.priority}, Remaining_Days: {self.remaining_days}"
    
class PersonalTask (Task):
    def __init__(self, task_id, task_name, deadline, status="Pending"):
        super().__init__(task_id, task_name, deadline, status)
        self.priority = "Low"

    def color_your_task(self):
        self.color = "Blue"

class WorkTask (Task):
    def __init__(self, task_id, task_name, deadline, status= "Pending"):
        super().__init__(task_id, task_name, deadline, status)
        self.priority = "High"

    def color_your_task(self):
        self.color = "Red"
