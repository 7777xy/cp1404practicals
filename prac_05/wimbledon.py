"""
Game, Set, Match
Estimate: 30 minutes
Actual:  45 minutes
"""

import csv

FILENAME = "wimbledon.csv"


def main():
    """print the champions and the winning countries from the file."""
    name_to_number = {}
    data = []
    countries = set()
    get_data(data)
    calculate_winning_time(name_to_number, data)
    print("Wimbledon Champions: ")
    for name, number in name_to_number.items():
        print(f"{name} {number}")
    print()
    country = collect_winning_country(countries, data)
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(country)


def get_data(data):
    """Get data from the csv file."""
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        text = csv.reader(in_file)
        next(text)
        for record in text:
            data.append(record)


def collect_winning_country(countries, data):
    """Collect winning countries."""
    for part in data:
        countries.add(part[1])
    countries = sorted(countries)
    country = ', '.join(countries)
    return country


def calculate_winning_time(name_to_number, data):
    """Calculate winning times."""
    for part in data:
        if part[2] in name_to_number:
            name_to_number[part[2]] += 1
        else:
            name_to_number[part[2]] = 1


main()
