password = input("Enter password: ")

result = []

# digit, upper, alpha = False
num_count = 0
char_count = 0
upper_count = 0

if len(password) >= 8:
    result.append(True)

    for letter in password:
        if letter.isdigit():
            num_count += 1
        elif letter.isupper():
            upper_count += 1
        elif letter.isalpha():
            char_count += 1

    if num_count >= 1 and char_count >= 1 and upper_count >= 1:
        result.append(True)
    else:
        result.append(False)

    print(all(result))
    if all(result):
        print("Strong Password")
    else:
        print("Weak Password")
else:
    # result.append(False)
    print("Password should be minimum 8 characters long.")


