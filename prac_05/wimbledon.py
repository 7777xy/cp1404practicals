"""
Game, Set, Match
Estimate: 30 minutes
Actual:   40 minutes
"""

import csv


def main():
    filename = "wimbledon.csv"
    name_to_number = {}
    countries = set()
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        text = csv.reader(in_file)
        next(text)
        process_data(name_to_number, text, countries)
        print_champion(name_to_number)
        print()
        print_winning_country(countries)


def process_data(name_to_number, text, countries):
    """Calculate the winning times and add winning countries."""
    for record in text:
        if record[2] in name_to_number:
            name_to_number[record[2]] += 1
        else:
            name_to_number[record[2]] = 1
        countries.add(record[1])


def print_champion(name_to_number):
    """Print the names and times of champions."""
    print("Wimbledon Champions: ")
    for name, number in name_to_number.items():
        print(f"{name} {number}")


def print_winning_country(countries):
    """Print countries that won the Wimbledon."""
    countries = sorted(countries)
    length = len(countries)
    country = ', '.join(countries)
    print(f"These {length} countries have won Wimbledon: ")
    print(country)


main()

