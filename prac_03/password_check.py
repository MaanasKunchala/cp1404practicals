def main():
    min_length = 8
    password = input("Enter a password: ")
    password = get_password(min_length, password)
    print_asterisks(password)


def get_password(min_length, password):
    while len(password) < min_length:
        print("Password should have a minimum of eight characters. Try again.")
        password = input("Enter a password: ")
    return password


def print_asterisks(password):
    print("*" * len(password))


main()
