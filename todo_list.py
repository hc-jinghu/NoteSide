# properties of a todo list
# A todo list will contain a list of tasks

from task import task as tsk

class todo_list(tsk):
    def __init__(self, desc=None, is_complete=False, title="TODO LIST", num_tsk=0, tasks=None):
        super().__init__(desc, is_complete)
        self.title=title
        self.num_tsk=num_tsk
        self.tasks=tasks

    def addTsk(self):
        self.desc=input("enter task: ")
        self.num_tsk+=1
    
    def complete_tsk(self):
        self.is_complete=True

    def print_list(self):
        # print list of tasks
        for task in self.tasks:
            print(task) 