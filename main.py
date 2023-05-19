# main program of todo_list

import PySimpleGUI as sg
from todo_list import todo_list as list

layout = [
    [sg.Input("Add a Task", key = "-INPUT-")],
    [sg.Button("ADD", key = "-ADD-")]
]
window = sg.Window("ToDo", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED():
        break

window.close()
