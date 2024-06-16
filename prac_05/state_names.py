"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention

valid_input = False
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)
max_length = max([len(code) for code in CODE_TO_NAME.keys()])
for code, name in CODE_TO_NAME.items():
    print(f"{code:{max_length}} is {name}")
while not valid_input:
    try:
        state_code = input("Enter short state: ").upper()
        while state_code != "":
            print(state_code, "is", CODE_TO_NAME[state_code])
            state_code = input("Enter short state: ").upper()
        valid_input = True
    except KeyError:
        print("Invalid short state")

