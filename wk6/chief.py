from taskScheduling import PersonalTask, WorkTask
from taskEditing import TaskEditing
from taskTracking import TaskTracking

class TaskManagement:
    
    def __init__ (self, task):
        self.task_list = []
        
    def add_task(self, task):
        self.task_list.append(task)

    def display_tasks(self):
        for task in self.task_list:
            print(task)
            pass

t1 = TaskManagement()
te = TaskEditing(t1)
tt = TaskTracking(t1)

p1 = PersonalTask(1, "P1", "2024-03-30", "Pending")
w1 = WorkTask(2, "W2", "2024-03-28", "Pending")
t1.add_task(p1)
t1.add_task(w1)

te.set_task_status(1, "In Progress")
te.mark_status_completed(2)

tt.get_task_color(1)
t1.display_tasks()

