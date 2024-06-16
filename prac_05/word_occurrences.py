"""
Word Occurrences
Estimate: 20 minutes
Actual:   35 minutes
"""

word_to_number = {}
text = input("Text: ")
parts = text.split(" ")
parts.sort()
for word in parts:
    if word in word_to_number:
        word_to_number[word] += 1
    else:
        word_to_number[word] = 1
max_length = max([len(part) for part in parts])
for word, number in word_to_number.items():
    print(f"{word:{max_length}} : {number}")

