# NoteSide
A simple to-do list software using python, PySimpleGui, and Docker

Main purpose:
Allows user to make a list of ToDo tasks, check and uncheck them depending on the completion status. 

Planned functions for the future:
- Delete checklist item
- Multiple ToDo lists
- urgent status
- calendar

## How to run program?
From VSCode: 
 - Dependencies: `Python 3.11.3`
 - Download or clone the repository and run `main.py`

From Docker: 
 - Dependencies: `Docker`, `XQuartz` for macOS
 - Download or clone the repository
 - Run command `xhost +localhost`
 - Run command `docker-compose up`
 - After you shutdown the program, run command `xhost -localhost`

