import random

LOWEST_NUMBER = 0
LOWER_NUMBER = 50
HIGHER_NUMBER = 90
HIGHEST_NUMBER = 100


def main():
    """Print the category according to the score."""
    score = validate_score()
    category = determine_category(score)
    print(category)
    random_score = random.randint(LOWEST_NUMBER, HIGHEST_NUMBER)
    random_score_category = determine_category(random_score)
    print(random_score_category)


def validate_score():
    """Validate the score"""
    score = float(input("Enter score: "))
    while score < LOWEST_NUMBER or score > HIGHEST_NUMBER:
        print("Invalid score.")
        score = float(input("Enter score: "))
    return score


def determine_category(score):
    """Determine the category."""
    if score < LOWER_NUMBER:
        return "Bad"
    if score < HIGHER_NUMBER:
        return "Passable"
    return "Excellent"


main()
