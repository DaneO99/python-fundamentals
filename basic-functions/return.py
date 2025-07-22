
# def add(x, y):
#     z = x + y
#     return z

# def subtract(x, y):
#     z = x - y
#     return z

# def multiply(x, y):
#     z = x * y
#     return z
# def divide(x, y):
#     z = x / y
#     return z

# print(add(21.5,22))
# print(subtract(21.5,22))
# print(multiply(21.5,22))
# print(divide(21.5,22))

def create_name(firstName, lastName):
    firstName = firstName.capitalize()
    lastName = lastName.capitalize()
    return firstName + " " + lastName

full_name = create_name("dane" , "fitzgerald")
print(full_name)
