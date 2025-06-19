import os

print (" Create a To-Do List")

todo_list = []

if os.path.exists("Todo.txt"):
    with open("Todo.txt", "r") as f:
        todo_list = [f.read()]

def cmd():
    print ("1) Add Task\n2) View Task\n3) Update Task\n4) Delete Task\n5) Exit\n")

def save_tasks():
    with open("Todo.txt", "w") as f:
        for item in todo_list:
            f.write(item + "\n")

def add_task ():
    task = input("Enter the task: ")
    todo_list.append(task)
    save_tasks()

    print("Task added!")


def view_task():

        for index,data in enumerate (todo_list,start =1):
            print (index,data)

def update_task():
    view_task()
    if todo_list:
        try:
            task_value = int(input("Enter the number of the task you want to update: "))
            if task_value < 1 or task_value > len(todo_list):
                raise ValueError(f"{task_value} is invalid or doesn't exist. Please enter a valid Value.")

            new_taskvalue = input("Enter the new task: ")
            old_task = todo_list[task_value - 1]
            todo_list[task_value - 1] = new_taskvalue
            print(f"'{old_task}' has been updated to '{new_taskvalue}'.")

        except ValueError as e:
            print(f"Error: {e}")


def delete_task():
    view_task()
    if todo_list:
        try:
            task_value = int(input("Enter the value for task-"))
            
            if task_value < 1 or task_value > len (todo_list):
                 raise ValueError (f"{task_value} is invalid or doesn't exist. Please enter a valid Value.")
            
            remove = todo_list.pop(task_value -1 )
            print (f"{remove} is removed from the list.")
        except ValueError as e:
             print(f"{e}")


while True:

    cmd()
    choice = input (" Enter your choice (1-4):- ")


    if choice == "1":
        add_task()

    elif choice == "2":
        view_task()   

    elif choice == "3":
          update_task()       

    elif choice == "4":
         delete_task() 

    elif choice == "5":
        print ("Thanks For Viewing") 
        break

    else:
        print("Enter a valid option. Thank You!")        




            



