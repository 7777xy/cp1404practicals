from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a Silver Service Taxi object, based on parent class Taxi."""
    flagfall = 4.50

    def __init__(self, name="", fuel=0, fanciness=0):
        """Initialize a Silver Service Taxi object."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness

    def get_fare(self):
        """Get fare like parent Taxi, but add the flagfall in the answer."""
        return super().get_fare() + self.flagfall
