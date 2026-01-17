import functions
import FreeSimpleGUI as sg

layout=[
    [sg.Text("Type in a to-do")],
    [sg.InputText(tooltip="Enter todo", key="todo"),sg.Button("Add")],
    [sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=(45,10)), sg.Button("Edit"), sg.Button("Complete")],
    [sg.Button("Exit", key="Exit")],
]

window = sg.Window('My To-Do App', layout, font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(f"1. {event}")
    print(f"2. {values}")
    match event:
        case "Add":
            todos = functions.get_todos()
            todo_num = len(todos) + 1
            new_todo  = f"{todo_num}. {values['todo']}"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]

            number, _ = todo_to_edit.split(". ", 1)
            new_todo = f"{number}. {values['todo']}"

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo

            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Complete":
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
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            exit()


window.close()