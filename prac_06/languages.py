from prac_06.programming_language import ProgrammingLanguage

languages = []


def main():
    """Display the dynamically typed language."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    languages.append(python)
    languages.append(ruby)
    languages.append(visual_basic)



main()
