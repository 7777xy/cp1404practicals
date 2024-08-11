"""
Estimate time: 1h
Actual time: 7h
"""
import datetime
from prac_07.project import Project
from operator import attrgetter

FILENAME = "projects.txt"
MENU = ("- (L)oad project\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n"
        "- (U)pdate project\n- (Q)uit")
MINIMUM_PROJECT_CHOICE = 0
MINIMUM_PERCENTAGE = 0
MAXIMUM_PERCENTAGE = 100
MINIMUM_PRIORITY = 0
MAXIMUM_PRIORITY = 20
MINIMUM_COST_ESTIMATE = 0
MAXIMUM_COST_ESTIMATE = 999999


def main():
    """Play the program according to the menu."""
    data = []
    load_data(data, FILENAME)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(data)} projects from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            load_project(data)
        elif choice == "S":
            save_project(data)
        elif choice == "D":
            display_projects(data)
        elif choice == "F":
            filter_project(data)
        elif choice == "A":
            add_new_project(data)
        elif choice == "U":
            update_project(data)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    save_data(data, FILENAME)
    print("Thank you for using custom-built project management software.")


def save_project(data):
    """Save project."""
    new_saving_filename = input("New saving filename: ")
    save_data(data, new_saving_filename)


def load_project(data):
    """Load project."""
    new_loading_filename = input("New filename:")
    load_data(data, new_loading_filename)


def filter_project(data):
    """Filter project by date."""
    filtered_projects = []
    filter_date = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(filter_date, "%d/%m/%Y").date()
    for project in data:
        project.start_date = datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date()
        if filter_date <= project.start_date:
            filtered_projects.append(project)
        else:
            project.start_date = project.start_date.strftime("%d/%m/%Y")
    filtered_projects.sort(key=attrgetter("start_date"))
    for filtered_project in filtered_projects:
        filtered_project.start_date = filtered_project.start_date.strftime("%d/%m/%Y")
        print(filtered_project)


def update_project(data):
    """Update project."""
    for i, new_project in enumerate(data):
        print(f"{i} {new_project}")
    project_choice = validate_detail("Project choice: ", int, MINIMUM_PROJECT_CHOICE, len(data) - 1)
    print(data[project_choice])
    update_percentage(data, project_choice)
    update_priority(data, project_choice)


def update_priority(data, project_choice):
    """Update priority."""
    is_valid_input = False
    while not is_valid_input:
        try:
            new_priority = input("New Priority: ")
            if new_priority != "":
                if int(new_priority) < MINIMUM_PRIORITY or int(new_priority) > MAXIMUM_PRIORITY:
                    print("Error priority.")
                else:
                    data[project_choice].priority = int(new_priority)
                    is_valid_input = True
            else:
                is_valid_input = True
        except ValueError:
            print("Priority should be a number.")


def update_percentage(data, project_choice):
    """Update percentage."""
    is_valid_input = False
    while not is_valid_input:
        try:
            new_percentage = input("New Percentage: ")
            if new_percentage != "":
                if int(new_percentage) < MINIMUM_PERCENTAGE or int(new_percentage) > MAXIMUM_PERCENTAGE:
                    print("Error percentage.")
                else:
                    data[project_choice].completion_percentage = int(new_percentage)
                    is_valid_input = True
            else:
                is_valid_input = True
        except ValueError:
            print("Percentage should be a number.")


def save_data(data, filename):
    """Save data into the txt file."""
    saving_message = input("Would you like to save to projects.txt? ")
    if saving_message == "Yes":
        with open(filename, 'w') as out_file:
            print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
            for project in data:
                print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t"
                      f"{project.completion_percentage}", file=out_file)


def add_new_project(data):
    """Add new project."""
    print("Let's add a new project")
    name = input("Name: ").title()
    start_date = input("Start date (dd/mm/yy): ")
    start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
    priority = validate_detail("Priority: ", int, MINIMUM_PRIORITY, MAXIMUM_PRIORITY)
    cost_estimate = validate_detail("Cost estimate: $", float, MINIMUM_COST_ESTIMATE, MAXIMUM_COST_ESTIMATE)
    completion_percentage = validate_detail("Percent complete: ", int, MINIMUM_PERCENTAGE, MAXIMUM_PERCENTAGE)
    new_project = Project(name, start_date.strftime("%d/%m/%Y"), priority, cost_estimate, completion_percentage)
    data.append(new_project)


def validate_detail(message, detail_type, minimum_limit, maximum_limit):
    """Validate element."""
    while True:
        try:
            detail = detail_type(input(message))
            if detail < minimum_limit or detail > maximum_limit:
                print("It is out of the range.")
            else:
                break
        except ValueError:
            print("It should be a number.")
    return detail


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
