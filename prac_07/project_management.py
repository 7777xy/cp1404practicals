"""
Estimate time: 1h
Actual time:
"""

from prac_07.project import Project

FILENAME = "projects.txt"


def main():
    """Play the program according to the menu."""
    data = []
    load_data(data)


def load_data(data):
    """Load the data from the txt file."""
    with open(FILENAME) as in_file:
        in_file.readline().strip()
        for line in in_file:
            projects = line.strip().split('\t')
            name = projects[0]
            start_date = projects[1]
            priority = int(projects[2])
            cost_estimate = float(projects[3])
            completion_percentage = int(projects[4])
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            data.append(project)


main()
