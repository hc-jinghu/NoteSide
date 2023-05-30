# properties of a task:
# task id
# task description
# task status

class task:
    def __init__(self, id, desc=None, is_complete=False):
        self.id = id
        self.desc=desc
        self.is_complete=is_complete

    def print_task(self):
        print(f"{self.id}" + ": " + f"{self.desc}")