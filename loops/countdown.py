import time

my_time = int(input("Enter your countdown start time: "))

for x in range(my_time , 0, -1):
    seconds = x % 60
    minute = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minute:02}:{seconds:02}")
    time.sleep(1)
print("Time's up!")