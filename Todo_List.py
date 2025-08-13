class Todo_List:
    def __init__(self):
       self.file_name = "tasks.txt"
       self.tasks =[]
    def add_task(self,task):
        with open(self.file_name,"a") as f:
            f.write(task + "\n")
            self.tasks.append(task)
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
        print(f"Successfully deleted {task}\n")
                        


todo =Todo_List()
todo.view_task()
todo.delete_task("Homehahah")
todo.view_task()


