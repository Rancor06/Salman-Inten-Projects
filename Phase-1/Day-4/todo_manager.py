tasks = []
def add_task():
    x = input("Enter a task:")
    x = x.lower()
    tasks.append(x)
    print("Task added to the list!")
    print("\n")
    
def complete_task():
    i = int(input("Enter Number of tasks to complete:"))
    for key in range (i):
        x = input (f"Enter {key+1} task:")
        x = x.lower()
        if x in tasks:
            tasks.remove(x)
        else:
            print("Task is not present")
    print(f"{i} tasks completed")
    print("\n")

def pending_tasks():
    print("The remaining tasks are:")
    for idx, task in enumerate(tasks, start=1):
        task = task.capitalize()
        print(f"{idx} {task}")
    print("\n")
        
n=1
while (n!=0):
    print("TO DO LIST")
    print("-" * 20)
    print("1. Add Tasks         \t2. Complete Tasks\n3. View Pending Tasks\t4. Exit")
    x = int(input("Enter Option:"))
    print("\n")
    if x == 1:
        add_task()
    
    elif x == 2:
        complete_task()

    elif x == 3:
        pending_tasks()

    elif x == 4:
        n = 0 