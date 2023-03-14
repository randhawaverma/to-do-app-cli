# 1. Create empty list to store todos
todo_list = []

while True:
    # Asking user choice to add, show, edit or exit
    user_action = input("Type add, show, edit, complete or exit: ").strip()  # strip extra spaces

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todo_list.append(todo.title())
        case 'show':
            for i, item in enumerate(todo_list):
                print(f"{i + 1}. {item}")
        case 'edit':
            number = int(input("Enter number of todo to edit: "))
            new_todo = input("Enter updated todo: ")
            todo_list[number - 1] = new_todo
        case 'complete':
            number = int(input("Enter number of todo to edit: "))
            todo_list.pop(number - 1)
        case 'exit':
            break

print('Bye!')
