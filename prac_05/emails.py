"""
Emails
Estimate: 25 minutes
Actual:   30 minutes
"""


def main():
    """Print the names and emails according to the program."""
    names = []
    emails = []
    name_to_email = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        emails.append(email)
        answer = input(f"Is your name {name}? (Y/n) ").upper()
        if answer != "" and answer != "Y":
            name = input("Name: ")
        names.append(name)
        email = input("Email: ")
    print()
    for i in range(len(names)):
        name_to_email[names[i]] = emails[i]
    for name, email in name_to_email.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract name from email."""
    parts = email.split("@")
    parts = parts[0].split(".")
    name = ' '.join(parts).title()
    return name


main()

