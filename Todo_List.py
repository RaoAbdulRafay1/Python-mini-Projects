class Todo_List:
    def __init__(self):
       self.file_name = "tasks.txt"
       self.tasks =[]
    def add_task(self,task):
        with open(self.file_name,"a") as f:
            f.write(task + "\n")
            self.tasks.append(task)
        print(f"Successfully added {task}.")    
    def view_task(self):
        try:
            with open(self.file_name,"r") as f:
                tasks = f.readlines()
                if not tasks:
                    print("No tasks found.")
                else:
                    print("Tasks:")
                    for i, task in enumerate(tasks, 1):
                        print(f"{i}. {task.strip()}")
        except FileNotFoundError:
            print("No tasks found. Please add a task first.")
    def delete_task(self,task):
        with open(self.file_name,"r") as f:
            self.tasks =f.readlines()
            if task + "\n" in self.tasks:
                self.tasks.remove(task + "\n")
            else:
                print("Task not found")
        with open(self.file_name,"w") as f:
            f.writelines(self.tasks)
        print(f"Successfully deleted {task}")

print("========= Welcome to Todo app ==========")
print("1--Add Task")
print("2--View Task")
print("3--Delete Task")
print("4--Exit ")
todo = Todo_List()
check = 1
while  check:
    choice = input("Enter your choice :")
    if choice == "1":
        task = input("Enter Task :")
        todo.add_task(task)
    elif choice =="2":
        todo.view_task()
    elif choice =="3":
        task =input("Enter Task you want to delete :")
        todo.delete_task(task)
    elif choice =="4":
        print("Exiting App.....")
        check = 0
    else:
        print("Invalid Option. Please choose valid option")
        
        

