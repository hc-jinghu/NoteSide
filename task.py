# properties of a task

class task:
    def __init__(self, desc=None, is_complete=False):
        self.desc=desc
        self.is_complete=is_complete

    def print_desc(self):
        print(self.desc)