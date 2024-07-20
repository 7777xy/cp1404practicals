"""
Estimate time: 1h
Actual time: 2.5h
"""
import datetime
from prac_07.project import Project
from operator import attrgetter

FILENAME = "projects.txt"
MENU = ("- (L)oad project\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n"
        "- (U)pdate project\n- (Q)uit")
INVALID_PROJECT_CHOICE = 0
MINIMUM_PERCENTAGE = 0
MAXIMUM_PERCENTAGE = 100
MINIMUM_PRIORITY = 0
MINIMUM_COST_ESTIMATE = 0


def main():
    """Play the program according to the menu."""
    data = []
    load_data(data, FILENAME)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(data)} projects from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "D":
            display_projects(data)
        elif choice == "L":
            load_project(data)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    save_data(data, FILENAME)
    print("Thank you for using custom-built project management software.")


def load_project(data):
    """Load project."""
    new_loading_filename = input("New filename:")
    load_data(data, new_loading_filename)


def save_data(data, filename):
    """Save data into the txt file."""
    saving_message = input("Would you like to save to projects.txt? ")
    if saving_message == "Yes":
        with open(filename, 'w') as out_file:
            print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
            for project in data:
                print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t"
                      f"{project.completion_percentage}", file=out_file)


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


def load_data(data, filename):
    """Load the data from the txt file."""
    with open(filename) as in_file:
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
