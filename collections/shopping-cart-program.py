foods = []
prices = []
total = 0

while True:
    food = input("What food would you like to buy (q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"What is the price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("\n----- Your Cart ----- ")
for food, price in zip(foods, prices):
    print(f"{food}: ${price:.2f}")
    total += price

print(f"\nYour pre-tax total is: ${total:.2f}")

# Texas Sales Tax (8.25%)
sales_tax_rate = 0.0825
sales_tax = total * sales_tax_rate
post_tax_total = total + sales_tax

print(f"Sales tax (8.25%): ${sales_tax:.2f}")
print(f"Your total with tax is: ${post_tax_total:.2f}")
