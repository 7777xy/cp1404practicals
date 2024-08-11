"""
Estimated duration time: 35 min
Current time: 11:30
Finished time: 12:20
Actual duration time: 50 min
"""
from prac_06.guitar import Guitar

guitars = []


def main():
    """Get and display guitar according to the class Guitar."""
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print("My guitars!")
    get_guitar()
    print()
    print("... snip ...")
    print()
    display_guitar()


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


def display_guitar():
    """Display details of the guitar."""
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
