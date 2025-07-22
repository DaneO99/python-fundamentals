
menu = {}
add_more = True

while add_more:
    key = input("Enter an item sold at the concession stand(q to quit): ")
    if key.lower() == 'q':
        add_more = False
    else:
        value = float(input(f"Enter the price of {key}: "))
        menu[key] = value

for key, value in menu.items():
    print(f"{key} ----- {value}")
