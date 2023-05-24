# main program of NoteSide

import PySimpleGUI as sg
# from todo_list import todo_list as list

listLayout = [
    [sg.Input(key = "-INPUT-"), sg.Button("ADD", key="-ADD-")],
    [sg.TabGroup([[sg.Tab("ToDo", [], key="-TASK_VIEW-")]], expand_x=True, key="-TABGROUP-")]
]
window = sg.Window("NoteSide", listLayout, use_default_focus=False, font="15")

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    if event == "-ADD-":
        task = values["-INPUT-"]
        if task != "":
            window.extend_layout(window["-TASK_VIEW-"], [[sg.Checkbox(task)]])

window.close()

