from prac_06.guitar import Guitar

guitars = []


def main():
    """Get and display guitar according to the class Guitar."""
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print("My guitars!")
    get_guitar()


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


main()
