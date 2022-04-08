def main():
    numbers = []
    get_numbers(numbers)

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers)/len(numbers)}")


def get_numbers(numbers):
    for i in range(0, 5):
        number = int(input("Number: "))
        numbers.append(number)


def main_2():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    username = input("Username: ")
    verify_username(username, usernames)


def verify_username(username, usernames):
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()
main_2()