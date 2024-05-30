def main():
    """Print asterisks as long as the password."""
    minimum_length = int(input("Minimum length: "))
    password = validate_password(minimum_length)
    print_asterisks(password)


def print_asterisks(password):
    """Print the asterisks according to the length of password."""
    print("*" * len(password))


def validate_password(minimum_length):
    """Validate the password."""
    password = input("Password: ")
    while len(password) < minimum_length:
        print("Error password.")
        password = input("Password: ")
    return password


main()
