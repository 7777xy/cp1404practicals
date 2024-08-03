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
            current_taxi = get_current_taxi(current_taxi, taxis)
        elif choice == 'd':

        else:
            print("Invalid option")

        print(f"Bill to date: ${bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()



def get_current_taxi(current_taxi, taxis):
    """Choose the taxi from the given taxis."""
    display_taxi_detail("Taxis available:", taxis)
    try:
        current_taxi = int(input("Choose taxi: "))
        if current_taxi < LOWEST_TAXI_SEQUENCE_NUMBER or current_taxi > len(taxis) - 1:
            print("Invalid taxi choice")
            current_taxi = None
    except ValueError:
        print("It should be an integer.")
    return current_taxi



def display_taxi_detail(message, taxis):
    """Display details of each taxi."""
    print(message)
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
