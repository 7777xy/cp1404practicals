from prac_09.unreliable_car import UnreliableCar

LOWEST_DRIVING_DISTANCE = 0

unreliable_car = UnreliableCar(name="Audi", fuel=10, reliability=50)
driving_distance = unreliable_car.drive(20)
if driving_distance != LOWEST_DRIVING_DISTANCE:
    print("The car drives.")
else:
    print("The car does not drive.")
