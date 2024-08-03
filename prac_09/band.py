class Band:
    """Represent a Band object."""
    def __init__(self, name=""):
        """Initialise a Band instance."""
        self.name = name
        self.members = []

    def add(self, member):
        """Add the member into the members."""
        self.members.append(member)

    def play(self):
        """Display the details according to whether it has instruction."""
        for member in self.members:
            message = member.play()
            print(message)

    def __str__(self):
        """Return a string representation of a Band object."""
        output_message = ','.join(str(member) for member in self.members)
        return f"{self.name} ({output_message})"
