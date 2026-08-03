

tasks=[]
del_tasks=[]
def out_look():
    print("=======TO DO LIST=======")
    print("1.add_task")
    print("2.view_task")
    print("3.delete_task")
    print("4.show_delete_task")
    print("5.restore_delete_task")
    print("6.delete_task_permanently")
    print("7.save_task")
    print("8.exit")
    print()
    print("========================")

def add_task():
    task=input("enter your tasks:")
    print(f"your added task is :{task} ")
    tasks.append(task)
def view_task():
    if len(tasks)!=0:
        for i in range(len(tasks)):
            print(f"{i+1}.{tasks[i]}")
    else:print("no tasks added yet")
def delete_task():
    if len(tasks)!=0:
        for i in range(len(tasks)):
            print(f"{i+1}.{tasks[i]}")
        Del=int(input("enter index.no of the task to want to delete:"))
        if 0>Del>=len(tasks):
            print("invalid number")
        else:
            del_task=tasks.pop(Del-1)
            del_tasks.append(del_task)
            print(f"your task has {del_task} successfully deleted")
    else:print("no tasks added yet")
def show_delete_task():
    if len(del_tasks)!=0:
        for i in range(len(del_tasks)):
            print(f"{i+1}.{del_tasks[i]}")
    else:print("no deleted tasks yet")
def delete_task_permanently():
    if len(tasks)!=0:
        for i in range(len(tasks)):
            print(f"{i+1}.{tasks[i]}")
        Del=int(input("enter index.no of the task to want to delete:"))
        if  0>Del>=len(tasks):
            print("invalid number")
        else:
            del_task=tasks.pop(Del-1)
            print(f"you deleted the task {del_task} permanently")
    else:print("no tasks added yet")
def restore_delete_task():
    if len(del_tasks)!=0:
        for i in range(len(del_tasks)):
            print(f"{i+1}.{del_tasks[i]}")
        restore_task=int(input("enter index.no of the task to want to restore:"))
        if 0>=restore_task>=len(del_tasks):
            print("invalid number")
        else:
            task=del_tasks[restore_task-1]
            tasks.append(task)
            print(f"you restored the task:{task}")
            del_tasks.pop(restore_task-1)
    else:
        print("no deleted tasks yet")

while True:
    out_look()
    task_selection = int(input("enter index.no of the list you to want to do:"))
    if task_selection==1:
        add_task()
    elif task_selection==2:
        view_task()
    elif task_selection==3:
        delete_task()
    elif task_selection==4:
        show_delete_task()
    elif task_selection==5:
        restore_delete_task()
    elif task_selection==6:
        delete_task_permanently()
    elif task_selection==7:
        pass
    elif task_selection==8:
        print("save all your files,if you want to see them again when you visit again ")
        conform = input("conform exit(yes/no):")
        if conform == "yes":
           break
        else: pass
    elif task_selection!=range(1,9):
        print("you entered a wrong number.")

