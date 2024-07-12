"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
User not input a valid number in the numerator and denominator.

2. When will a ZeroDivisionError occur?
User input 0 in the denominator.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
DIVISION_ERROR_NUMBER = 0
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == DIVISION_ERROR_NUMBER:
        print("Denominator can not be zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
