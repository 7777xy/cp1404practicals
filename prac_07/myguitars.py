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
    get_guitar()
    save_guitar()


def save_guitar():
    """Save guitars in the csv file."""
    with open(FILENAME, 'w') as out_file:
        for guitar in guitars:
            print(guitar, file=out_file)


def get_guitar():
    """Get the guitar by inputting the details."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name=name, year=year, cost=cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        print()
        name = input("Name: ")


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
