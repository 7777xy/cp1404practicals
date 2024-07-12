"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
LOW_PERCENT_BONUS = 0.1
HIGH_PERCENT_BONUS = 0.15
LOWEST_SALES = 0
SALE = 1000
sales = float(input("Enter sales: $"))
while sales >= LOWEST_SALES:
    if sales < SALE:
        bonus = LOW_PERCENT_BONUS
    else:
        bonus = HIGH_PERCENT_BONUS
    print(bonus * sales)
    sales = float(input("Enter sales: $"))
print("Ending.")