unit = input("What unit do you want to use (F or C) ")
temp = float(input("Okay and what is the current temp in your area "))

if unit == 'C' or unit == 'c':
    temp = round((9 * temp) / 5 + 32, 2)
    print(f"The temp in your area in farenheit is {temp}")
elif unit == "f" or unit == "F":
    temp = round((temp - 32 ) * 5 / 9, 2)
    print(f"The temp in your are in celcius is {temp}")
else:
    print("Invalid unit")