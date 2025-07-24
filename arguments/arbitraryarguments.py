
# # def add(*args):
# #     total = 0
# #     for arg in args:
# #         total += arg
# #     return total

# # print(add(2,2,2,2))

# def display_name(*name):
#     for letter in name:
#         print(letter, end= " ")

# display_name("Dane", "Fitzgerald")

# def print_address(**kwargs):
#     for value in kwargs.values():
#         print(value, end= " ")


# street = input("Input the street address: ")
# city = input("Enter the city: ")
# state = input("Enter the state: ")
# zip_code = input("Enter the zip code: ")
# print()
# print_address(street = street,
#                city = city,
#                 state = state,
#                 zip_code = zip_code)

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end= " ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip_code')}")


shipping_label("Mr." , "Dane" , "Fitzgerald",
               street = "1234 Fake St",
               city = "Fake",
               state = "TX",
               zip_code = "12345",
               pobox = "PO Box 1001")
