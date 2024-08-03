from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Represent an Unreliable Car object, based on parent class Car."""
    def __init__(self, name, fuel, reliability):
        """Initialize an Unreliable Car object."""
        super().__init__(name, fuel)
        self.reliability = reliability

