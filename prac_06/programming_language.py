class ProgrammingLanguage:
    """Represent a Programming Language object."""
    def __init__(self, name="", typing="", reflection="", year=0):
        """Initialise a programming language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __is_dynamic__(self):
        """Check whether programming language is dynamically typed or not."""
        return self.typing == "Dynamic"


