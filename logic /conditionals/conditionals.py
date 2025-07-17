
num = 1
a = 7
b = 4
age = 21

print("Positive" if num > 0 else "Negative")
print("Even" if num % 2 == 0 else "Odd")

max_num = a if a > b else b
min_num = a if a < b else b

print(max_num)
print(min_num)

status = "Adult" if age >= 18 else "Child"
print(status)