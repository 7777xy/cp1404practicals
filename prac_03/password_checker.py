"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
IS_SPECIAL_CHARACTER_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
MIN_DIGIT_NUMBER = 0
MIN_LOWER_NUMBER = 0
MIN_UPPER_NUMBER = 0
MIN_SPECIAL_NUMBER = 0


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0
    for character in password:
        # TODO: count each kind of character (use str methods like isdigit)
        pass
        if character.isdigit():
            number_of_digit = number_of_digit + 1
        if character.islower():
            number_of_lower = number_of_lower + 1
        if character.isupper():
            number_of_upper = number_of_upper + 1
        if character in SPECIAL_CHARACTERS:
            number_of_special = number_of_special + 1

    if number_of_digit == MIN_DIGIT_NUMBER:
        return False
    if number_of_lower == MIN_LOWER_NUMBER:
        return False
    if number_of_upper == MIN_UPPER_NUMBER:
        return False
    if number_of_special == MIN_SPECIAL_NUMBER and IS_SPECIAL_CHARACTER_REQUIRED:
        return False

    # TODO: if any of the 'normal' counts are zero, return False

    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero

    # if we get here (without returning False), then the password must be valid
    return True


main()
