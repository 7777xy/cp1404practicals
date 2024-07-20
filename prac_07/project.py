COMPLETED_PERCENTAGE = 100


class Project:
    """Represent a Project object."""
    def __init__(self, name="", start_date="", priority=0, cost_estimate=0, completion_percentage=0):
        """Initialize a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Display the details of the project."""
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:.2f},"
                f" completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Compare the priority in order to sort project."""
        return self.priority < other.priority

    def __is_completed__(self):
        """Test the project is completed or not."""
        return self.completion_percentage == COMPLETED_PERCENTAGE
