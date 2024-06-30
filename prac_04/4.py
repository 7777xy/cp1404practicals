valid_input = False
while not valid_input:
    try:
        page = int(input("Number of Pages: "))
        if page <= 0:
            print("Number must be > 0")
        else:
            valid_input = True

    except ValueError:
        print("Invalid input - please enter a valid number")
