
capitals = {"Texas" : "Austin" , "Alabama" : "Montgomery" , "Alaska" : "Juneau" , "Arizona" : "Phoenix"}

# print(capitals.get("Texas"))
#adds a new state and capital
capitals.update({"Arkansas" : "Little Rock"})
#changes the texas capital to dallas
# capitals.update({"Texas" : "Dallas"})

# capitals.pop("Alabama")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()
# print(keys)
# print()
# print(capitals)

for key in capitals.keys():
    print(key)
print()

for value in capitals.values():
    print(value)
print()
for key, value in capitals.items():
    print(key, value)
