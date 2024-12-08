LOWEST_NUMBER = 0
LOWER_NUMBER = 50
HIGHER_NUMBER = 90
HIGHEST_NUMBER = 100


def main():
    """Play the program according to the menu."""
    menu = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
    print(menu)
    score = validate_score()
    option = input("Choice: ").lower()
    while option != "q":
        if option == "g":
            score = validate_score()
        elif option == "p":
            category = determine_category(score)
            print(category)
        elif option == "s":
            show_stars(score)
        else:
            print("Error option.")
        print(menu)
        option = input("Choice: ").lower()
    print("farewell.")


def show_stars(score):
    """Print as many stars as the score."""
    print("*" * score)


def validate_score():
    """Validate the score."""
    score = int(input("Enter a score(0-100): "))
    while score < LOWEST_NUMBER or score > HIGHEST_NUMBER:
        print("Invalid score.")
        score = int(input("Enter a score(0-100): "))
    return score


def determine_category(score):
    """Determine the category."""
    if score < LOWER_NUMBER:
        return "Bad"
    if score < HIGHER_NUMBER:
        return "Passable"
    return "Excellent"


main()
