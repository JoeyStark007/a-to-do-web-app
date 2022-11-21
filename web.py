import streamlit as st
import methods

todos = methods.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    methods.write_todos(todos)


st.title("Joseph's Todo App")
st.subheader("This is a to do app")
st.write("This app is to improve your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        methods.write_todos(todos)
        del st.session_state[todo]
        #needed for checkboxes
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a todo",
              on_change=add_todo, key='new_todo')


