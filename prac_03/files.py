# 1
FILENAME = "name.txt"
name = input("Name: ")
in_file = open(FILENAME, "w")
print(name, file=in_file)
in_file.close()

# 2
FILENAME = "name.txt"
out_file = open(FILENAME)
text = out_file.read().strip()
out_file.close()
print(F"Hi {text}!")

# 3
FILENAME = "numbers.txt"
number = 0
with open(FILENAME) as in_file:
    for line in range(2):
        text = in_file.readline().strip()
        number = number + int(text)
    print(number)

# 4
FILENAME = "numbers.txt"
number = 0
with open(FILENAME) as in_file:
    for line in range(3):
        text = in_file.readline().strip()
        number = number + int(text)
with open(FILENAME, "a") as out_file:
    print(number, file=out_file)
