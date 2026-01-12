import functions
import FreeSimpleGUI as sg

layout=[
    [sg.Text("Type in a to-do")],
    [sg.InputText(tooltip="Enter todo", key="todo"),sg.Button("Add")],
    [sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=(45,10)), sg.Button("Edit")],
]

window = sg.Window('My To-Do App', layout, font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
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
            new_todo = values["todo"]
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            todos = [f"{i + 1}. {todo.split('. ', 1)[-1]}\n" for i, todo in enumerate(todos)]
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break


window.close()