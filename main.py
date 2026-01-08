from functions import get_todos, write_todos
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now}")
while True:
    user_prompt = input("Type add, show, edit, complete or exit: ")
    user_prompt = user_prompt.strip()


    if user_prompt.startswith("add"):

            todo = user_prompt[4:]

            todos  = get_todos()


            todos.append(todo.capitalize() + '\n')

            write_todos(todos)

    elif user_prompt.startswith("show"):

            todos = get_todos()

            # new_list = [item.strip('\n') for item in todos] -> LIST COMPREHENSION

            for index, item in enumerate(todos, start=1):
                print(f"{index}. {item.strip('\n')}")

    elif user_prompt.startswith("edit"):
        try:
            todo_num = int(user_prompt[5:])
            todo_num = todo_num -1

            todos = get_todos()

            new_todo = input("Enter a new todo: ")

            todos[todo_num] = new_todo.capitalize() + '\n'
            write_todos(todos)

        except ValueError:
            print("Invalid input")
            continue
    elif user_prompt.startswith("complete"):
        try:
            completed_num = int(user_prompt[9:])

            todos = get_todos("files/todos.txt")

            completed_num = completed_num - 1
            todos.pop(completed_num)
            write_todos(todos)
            print("task completed")
        except IndexError:
            print(f"that {completed_num} does not exist")
            continue
    elif user_prompt.startswith("exit"):
            print("Goodbye")
            break
    else:
        print("Invalid input")