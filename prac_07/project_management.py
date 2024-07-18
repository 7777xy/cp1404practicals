"""
Estimate time: 1h
Actual time:
"""

from prac_07.project import Project


FILENAME = "projects.txt"
MENU = ("- (L)oad project\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n"
        "- (U)pdate project\n- (Q)uit")


def main():
    """Play the program according to the menu."""
    data = []
    load_data(data)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(data)} projects from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "D":
            display_projects(data)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()


def display_projects(data):
    """Display completed projects and incomplete projects."""
    incomplete_projects = []
    completed_projects = []
    for project in data:
        if project.__is_completed__():
            completed_projects.append(project)
        else:
            incomplete_projects.append(project)
    display_partial_projects("Incomplete projects:", incomplete_projects)
    display_partial_projects("Completed projects:", completed_projects)


def display_partial_projects(message, partial_projects):
    """Display partial projects."""
    print(message)
    partial_projects.sort()
    for project in partial_projects:
        print(f" {project}")


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
