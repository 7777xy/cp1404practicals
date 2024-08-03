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
            bill = drive_car(bill, current_taxi, taxis)
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill}")
    display_taxi_detail("Taxis are now:", taxis)


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


def drive_car(bill, current_taxi, taxis):
    """Drive the car according to the distance."""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
    else:
        taxis[current_taxi].start_fare()
        distance = float(input("Drive how far? "))
        taxis[current_taxi].drive(distance)
        print(f"Your {taxis[current_taxi].name} trip cost you ${taxis[current_taxi].get_fare():.2f}")
        bill += taxis[current_taxi].get_fare()
    return bill


def display_taxi_detail(message, taxis):
    """Display details of each taxi."""
    print(message)
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
