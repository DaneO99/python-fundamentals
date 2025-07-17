temp = 75
is_sunny = True

if temp < 0:
    print("It is below freezing who cares about the sun")
elif 0 < temp <= 32:
    if is_sunny:
        print("It is freezing and sunny")
    else:
        print("It is freezing and not sunny")
elif 32 < temp <= 60:
    if is_sunny:
        print("It is cool and sunny outside")
    else:
        print("It is cool and not sunny")
elif 60 < temp <= 80:
    if is_sunny:
        print("It is warm and sunny outside")
    else:
        print("It is warm and not sunny")
elif 80 < temp <= 100:
    if is_sunny:
        print("It is hot and sunny")
    else:
        print("It is hot and not sunny outside")
else:
    print("Immediate death its so hot out")
