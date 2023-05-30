# properties of a task_list
# A task_list will contain a collection of tasks

import PySimpleGUI as sg
from task import task

class task_list:
    # task_list layout in PySimpleGUI
    layout = [
        [sg.Input(key = "-INPUT-"), sg.Button("ADD", key="-ADD-")],
        [sg.Text('', key="-ERRORMSG-")],
        [sg.TabGroup([[sg.Tab("ToDo", [], key="-TASK_VIEW-")]], expand_x=True, key="-TABGROUP-")]
    ]


    # task_counter is initialized to 0 so we start with an empty list every time
    def __init__(self, task_counter=0):
        self.collection=dict()
        self.task_counter=task_counter

    def addTsk(self, value):
        new_task = task(self.task_counter, value)
        self.collection[new_task.id]=new_task
        self.task_counter+=1
        #print("Add task f"{new_task.id}" + ": " + f"{new_task.desc}")

    def complete_tsk(self):
        self.is_complete=True

    def print_list(self):
        # print list of tasks
        for t in self.collection.values():
            t.print_task()
