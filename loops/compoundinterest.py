
principle = 0
rate = 0
time = 0 #Time is in years

while principle<= 0:
    principle = float(input("Enter the principle value: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero!")

while rate <= 0:
    rate = float(input("Enter the rate value: "))
    if rate <= 0:
        print("Interest rate can't be less than or equal to zero!")

while time <= 0:
    time = int(input("Enter the length of time: "))
    if time <= 0:
        print("Time can't be less than or equal to zero!")

total = principle * pow((1 + rate / 100) , time )
print(f"Balance after {time} year/s is : ${total:.2f}")