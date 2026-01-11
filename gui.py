import functions
import FreeSimpleGUI as sg

layout=[
    [sg.Text("Type in a to-do")],
    [sg.InputText(tooltip="Enter todo", key="todo"),sg.Button("Add")]
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
            new_todo  = f"{todo_num}. {values["todo"]}\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        # case sg.WIN_CLOSED:
        #     break


window.close()