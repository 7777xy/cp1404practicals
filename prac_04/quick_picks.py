import random

LOW_NUMBER = 1
HIGH_NUMBER = 45

numbers = []
quick_picks_number = int(input("How many quick picks? "))
for i in range(quick_picks_number):
    for j in range(6):
        number = random.randint(LOW_NUMBER, HIGH_NUMBER)
        while number in numbers:
            number = random.randint(LOW_NUMBER, HIGH_NUMBER)
        numbers.append(number)
        numbers.sort()
    for number in numbers:
        print(f"{number:>2}", end=" ")
    print()
    del numbers[0:]
