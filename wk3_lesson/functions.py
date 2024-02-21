#def salute(x):
#    print("goede morgen", x)
#print(salute("Adam"))


def task_addition():
    tasks = []
    count=0
    while count < 3 :
        user = input("Add a new task: ")
        tasks.append(user)
        count += 1
    return tasks
    
print(task_addition())