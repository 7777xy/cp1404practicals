"""
Estimated duration time: 30 min
Current time: 12:10
Finished time: 12:50
Actual duration time: 40 min
"""
from prac_06.programming_language import ProgrammingLanguage

languages = []


def main():
    """Display language according to the class Programming Language."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    languages.append(python)
    languages.append(ruby)
    languages.append(visual_basic)
    display_language()


def display_language():
    """Display the dynamically typed language."""
    print("The dynamically typed languages are:")
    for language in languages:
        if language.__is_dynamic__():
            print(language.name)


main()
