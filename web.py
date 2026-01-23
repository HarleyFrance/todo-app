import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo_arg = st.session_state["new_todo"]
    todos.append(todo_arg)
    functions.write_todos(todos)

def remove_todo(todo):
    todos.remove(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("Todos")
st.write("This app is to increase your productivity")


for todo in todos:
    st.checkbox(todo, key=todo, on_change=remove_todo, args=(todo,))

text = st.text_input(label="Enter new todo", label_visibility="hidden", placeholder="Add new todo", on_change=add_todo, key="new_todo")