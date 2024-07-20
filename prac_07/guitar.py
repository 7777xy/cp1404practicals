class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Display the details of guitar."""
        return f"{self.name},{self.year},{self.cost:.2f}"

    def __lt__(self, other):
        """Compare the guitar by year."""
        return self.year < other.year

