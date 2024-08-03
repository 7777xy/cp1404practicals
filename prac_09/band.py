class Band:
    """Represent a Band object."""
    def __init__(self, name=""):
        """Initialise a Band instance."""
        self.name = name
        self.members = []

    def add(self, member):
        """Add the member into the members."""
        self.members.append(member)

