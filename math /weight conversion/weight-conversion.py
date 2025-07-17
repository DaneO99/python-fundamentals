
weight = float(input("Enter your weight "))
unit = input("Is this unit it pounds(lbs) or kilograms(kgs) ")

if unit == "lbs" or unit == "pounds":
    weight /= 2.205
    print(f"You weigh {round(weight , 2)} in kgs")
elif unit == "kgs" or unit == "kilograms":
    weight *= 2.205
    print(f"You weigh {round(weight, 2)} in pounds ")
else:
    print("Invalid unit")