MINIMUM_LENGTH = 8


def main():
    """Print asterisks as long as the password."""
    password = validate_password()
    print_asterisks(password)


def print_asterisks(password):
    """Print the asterisks according to the length of password."""
    print("*" * len(password))


def validate_password():
    """Validate the password."""
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Error password.")
        password = input("Password: ")
    return password


main()
