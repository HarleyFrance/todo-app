import streamlit as st
import functions

todos = functions.get_todos()


st.title("My Todo App")
st.subheader("Todos")
st.write("This app is to increase your productivity")


for todo in todos:
    st.checkbox(todo)

text = st.text_input("",placeholder="Add new todo")