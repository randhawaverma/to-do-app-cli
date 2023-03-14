# 1. Create empty list to store todos
# todo_list = []

while True:
    # Asking user choice to add, show, edit or exit
    user_action = input("Type add, show, edit, complete or exit: ").strip()  # strip extra spaces

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            # todo_list.append(todo.title())
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
                todos.append(todo)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
                for i, item in enumerate(todos):
                    print(f"{i + 1}. {item}")
        case 'edit':
            number = int(input("Enter number of todo to edit: "))
            new_todo = input("Enter updated todo: ")
            todos[number - 1] = new_todo
        case 'complete':
            number = int(input("Enter number of todo to edit: "))
            todos.pop(number - 1)
        case 'exit':
            break

print('Bye!')
