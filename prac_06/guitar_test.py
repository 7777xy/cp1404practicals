"""
Estimated duration time: 20 min
Current time: 1:45
Finished time: 2:10
Actual duration time: 25 min
"""
from prac_06.guitar import Guitar


def main():
    """Test whether method work as expected or not."""
    gibson = Guitar("Gibson L-5 CES", 1922)
    another_guitar = Guitar("Another Guitar", 2013)
    print(f"{gibson.name} get_age() - Expected 100. Got {gibson.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 9. Got {another_guitar.get_age()}")
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")


main()
