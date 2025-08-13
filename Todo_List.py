class Todo_List:
    def __init__(self):
       self.file_name = "tasks.txt"
       self.tasks =[]
    def add_task(self,task):
        with open(self.file_name,"a") as f:
            f.write(task + "\n")
            self.tasks.append(task)

todo =Todo_List()
todo.add_task("Home")
todo.add_task("Homeworkk")
todo.add_task("Homehahah")

