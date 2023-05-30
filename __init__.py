# main program of NoteSide


import PySimpleGUI as sg
from task_list import task_list as t_list

new_list = t_list()

window = sg.Window("NoteSide", new_list.layout, use_default_focus=False, font="15")

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    if event == "-ADD-":
        task = values["-INPUT-"]
        if task != "":
            new_list.addTsk(task)
            window["-ERRORMSG-"].update("")
            window.extend_layout(window["-TASK_VIEW-"], [[sg.Checkbox(task)]])
        else:
            window["-ERRORMSG-"].update("Task cannot be empty")

window.close()

