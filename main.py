# main program of NoteSide

import PySimpleGUI as sg
# from todo_list import todo_list as list

taskLayout = [
    [sg.Checkbox("task1")],
    [sg.Checkbox("task2")]
]

listLayout = [
    [sg.Input(key = "-INPUT-"), sg.Button("ADD", key="-ADD-")],
    [sg.TabGroup([[sg.Tab("ToDo", taskLayout)]], expand_x=True, key="-TABGROUP-")]
]
window = sg.Window("NoteSide", listLayout, use_default_focus=False, font="15")

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    if event == "-ADD-":
        break
        # task = values["-INPUT-"]
        # taskLayout.append(sg.Checkbox(task))
        # print("add is clicked")
        

window.close()
