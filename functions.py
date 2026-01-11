FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    """Reads todos.txt file and returns list of todos"""
    with open(filepath, 'r') as file:
        todos = file.readlines()  # ['Cooking', 'Eating]
    return todos

def write_todos(todos_arg, filepath=FILEPATH):
    """Writes todos.txt file to todos.txt"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print(get_todos())
    print("hello")