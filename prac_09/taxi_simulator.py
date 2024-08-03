from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = 'q)uit, c)hoose taxi, d)rive'
LOWEST_TAXI_SEQUENCE_NUMBER = 0


def main():
    """Create a taxi simulator program by using other two classes."""
    current_taxi = None
    bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'c':

        elif choice == 'd':

        else:
            print("Invalid option")

        print(f"Bill to date: ${bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()


main()
