def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        yes_or_no = input(f"Is your name {name}? (Y/n) ").lower()
        if yes_or_no == "y" or yes_or_no == "yes" or yes_or_no == "":
            email_to_name[email] = name
        elif yes_or_no == "n" or yes_or_no == "no":
            name = input("Name: ")
            email_to_name[email] = name
        else:
            print("Invalid Input")
        email = input("Email: ")
    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name(email):
    parts_of_email = email.split("@")
    parts_of_name = parts_of_email[0].split(".")
    lowercase_name = " ".join(parts_of_name)
    name = lowercase_name.title()
    return name


main()
