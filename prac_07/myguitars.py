import csv
from prac_07.guitar import Guitar

FILENAME = "guitars.csv"
guitars = []


def main():
    """Load, display and save guitar."""
    load_guitar()
    print()
    guitars.sort()
    display_guitar()


def load_guitar():
    """Load guitars from csv file."""
    with open(FILENAME) as in_file:
        readers = csv.reader(in_file)
        for line in readers:
            name = line[0]
            year = line[1]
            cost = line[2]
            guitar = Guitar(name, year, float(cost))
            print(guitar)
            guitars.append(guitar)


def display_guitar():
    """Display guitars that are sorted by year."""
    for guitar in guitars:
        print(guitar)


main()
