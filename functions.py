FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    """Reads todos.txt file and returns list of todos"""
    with open(filepath, 'r') as file:
        return [line.strip() for line in file if line.strip()]


def write_todos(todos_arg, filepath=FILEPATH):
    """Writes todos.txt file to todos.txt"""
    with open(filepath, 'w') as file:
        file.write("\n".join(todos_arg))


if __name__ == "__main__":
    print(get_todos())
    print("hello")