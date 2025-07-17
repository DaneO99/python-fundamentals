import math

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

response = input("What do you want to do + , - , / , * : ")

if response == "+":
    print(x + y)
elif response == "-":
    print(x - y)
elif response == "/":
    print(x / y)
elif response == "*":
    print(x * y)
else:
    print("Invalid response.")