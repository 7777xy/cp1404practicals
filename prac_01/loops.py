"""a"""
for i in range(0, 101, 10):
    print(i, end=' ')
print()

"""b"""
for i in range(20, 0, -1):
    print(i, end=' ')
print()

"""c"""
LOWEST_NUMBER = 0
number = int(input("Number of stars: "))
while number <= LOWEST_NUMBER:
    print("Error number.")
    number = int(input("Number of stars: "))
for i in range(number):
    print("*", end="")
print()

"""d"""
LOWEST_NUMBER = 0
number = int(input("Number of stars: "))
while number <= LOWEST_NUMBER:
    print("Error number.")
    number = int(input("Number of stars: "))
for i in range(1, number + 1):
    print("*" * i)
print()