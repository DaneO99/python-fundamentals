# can do this with lists (like shown), tuples or sets

# fruits = ["apple" , "orange", "coconut" , "banana"]
# vegetables = ["celery", "carrot" , "potato"]
# meats = ["chicken" , "steak" , "fish"]

# groceries = [fruits , vegetables , meats]

# groceries = [["apple" , "orange", "coconut" , "banana"],
#             ["celery", "carrot" , "potato"],
#             ["chicken" , "steak" , "fish"]]

# #prints the grocery matrix in the form of [row][column]
# # print(groceries[0][1])
# for collection in groceries:
#     for item in collection:
#         print(item)
#     print()

num_pad = (("1" , "2" , "3"),
           ("4" , "5" , "6"),
           ("7" , "8" , "9"),
           ("*" , "0" , "#"))
for number in num_pad:
    for num in number:
        print(num , end= " ")
    print()
