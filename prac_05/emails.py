def main():
    email_to_name = {}
    email = input("Email: ")
    name = get_name(email)
    yes_or_no = input(f"Is your name {name}? (Y/n) ")


def get_name(email):
    parts_of_email = email.split("@")
    parts_of_name = parts_of_email[0].split(".")
    lowercase_name = " ".join(parts_of_name)
    name = lowercase_name.title()
    return name


main()