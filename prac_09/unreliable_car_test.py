from prac_09.unreliable_car import UnreliableCar

LOWEST_DISTANCE_DRIVEN = 0

unreliable_car = UnreliableCar(name="Audi", fuel=10, reliability=50)
distance_driven = unreliable_car.drive(20)
if distance_driven != LOWEST_DISTANCE_DRIVEN:
    print("The car drives.")
else:
    print("The car does not drive.")

