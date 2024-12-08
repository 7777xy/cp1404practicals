"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
LOWEST_NUMBER = 0
LOWER_NUMBER = 50
HIGHER_NUMBER = 90
HIGHEST_NUMBER = 100

score = float(input("Enter score: "))
while score < LOWEST_NUMBER or score > HIGHEST_NUMBER:
    print("Invalid score.")
    score = float(input("Enter score: "))
if score < LOWER_NUMBER:
    print("Bad")
elif score < HIGHER_NUMBER:
    print("Passable")
else:
    print("Excellent")
