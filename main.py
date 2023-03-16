# 1. Create empty list to store todos
# todo_list = []

while True:
    # Asking user choice to add, show, edit or exit
    user_action = input("Type add, show, edit, complete or exit: ").strip()  # strip extra spaces

    if 'add' in user_action:
        # todo = input("Enter a todo: ") + "\n"
        todo = user_action[4:]
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
            todos.append(todo.title() + "\n")
        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        # new_todos = [item.strip('\n') for item in todos]

        for i, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{i + 1}. {item}")

    elif 'edit' in user_action:
        number = int(user_action[5:])
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        # number = int(input("Enter number of todo to edit: "))
        new_todo = input("Enter updated todo: ") + "\n"
        todos[number - 1] = new_todo
        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        number = int(user_action[9:])
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        # number = int(input("Enter number of todo to edit: "))
        todo_to_remove = todos[number - 1].strip("\n")
        todos.pop(number - 1)
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
        message = f"Todo: {todo_to_remove} is marked as completed and removed from the list."
        print(message)
    elif 'exit' in user_action:
        break
    else:
        print("Command is not valid")

print('Bye!')
