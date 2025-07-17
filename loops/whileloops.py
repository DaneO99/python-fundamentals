
# name = input("Enter your name: ")

# while(name == ""):
#     print("You did not enter your name")
#     name = input("Please enter your name: ")
# print(f"Hello {name}")

# age = int(input("Enter your age: "))

# while age <= 100:
#     print(age)
#     age += 1

food = input("Enter a food you like ('q' to quit) ")

while food.lower() != 'q':
    print(f"{food}")
    food = input("Enter another food you like ('q' to quit) ")
