total_price = 0
DISCOUNT_PERCENTAGE = 0.1
DISCOUNT_PRICE = 100
LOWEST_NUMBER = 0
number = int(input("Number of items: "))
while number < LOWEST_NUMBER:
    print("Invalid number of items!")
    number = int(input("Number of items: "))
for i in range(number):
    price = float(input("Price of items: "))
    total_price = total_price + price
if total_price > DISCOUNT_PRICE:
    total_price = total_price - total_price * DISCOUNT_PERCENTAGE
print(f"Total price for {number} items is ${total_price:.2f} ")
