import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as filename:
        pass

sg.theme('DarkBlue')
layout=[
    [sg.Text('', key='clock')],
    [sg.Text("Type in a to-do")],
    [sg.InputText(tooltip="Enter todo", key="todo"),sg.Button("Add", size=10)],
    [sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=(45,10)), sg.Button("Edit"), sg.Button("Complete")],
    [sg.Button("Exit", key="Exit")],
]

window = sg.Window('My To-Do App', layout, font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    if event == sg.WIN_CLOSED:
        break
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            todo_num = len(todos) + 1
            new_todo  = f"{todo_num}. {values['todo']}"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update('')
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]

                number, _ = todo_to_edit.split(". ", 1)
                new_todo = f"{number}. {values['todo']}"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo

                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 20))
        case "Complete":
            try:
                if not values["todos"]:
                    continue  # nothing selected

                selected_todo = values["todos"][0]

                todos = functions.get_todos()
                index = todos.index(selected_todo)

                # Remove by index
                todos.pop(index)

                # Renumber todos
                renumbered_todos = []
                for i, todo in enumerate(todos, start=1):
                    _, text = todo.split(". ", 1)
                    renumbered_todos.append(f"{i}. {text}")

                functions.write_todos(renumbered_todos)
                window['todos'].update(values=renumbered_todos)
                window['todo'].update("")
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            exit()


window.close()