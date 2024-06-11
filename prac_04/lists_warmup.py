numbers = [3, 1, 4, 1, 5, 9, 2]
NEW_LASE_ELEMENT = 1

"""
numbers[0]   # 3 
numbers[-1]  # 2
numbers[3]   # 1
numbers[:-1] # [3, 1, 4, 1, 5, 9]
numbers[3:4] # [1]
5 in numbers # True
7 in numbers # False
"3" in numbers # False
numbers + [6, 5, 3] # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""

# 1
numbers[0] = "ten"

# 2
numbers[len(numbers) - 1] = NEW_LASE_ELEMENT

# 3
print(numbers[2:])

# 4
if 9 in numbers:
    print("9 is an element of numbers")
else:
    print("9 is not an element of numbers")
