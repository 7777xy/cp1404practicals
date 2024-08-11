GIVING_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Display the details of guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Calculate the age of guitar."""
        return GIVING_YEAR - self.year

    def is_vintage(self):
        """Check whether guitar is vintage or not."""
        return self.get_age() >= VINTAGE_AGE
