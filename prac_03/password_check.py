MIN_LENGTH = 8
password = input("Enter a password: ")
while len(password) < 8:
    print("Password should have a minimum of eight characters. Try again.")
    password = input("Enter a password: ")
print("*" * len(password))