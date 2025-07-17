userName = input("Input a username:")

if len(userName) > 12:
    print("Username is too long")
elif not userName.find(" ") == -1:
    print("Username cannot contain spaces")
elif not userName.isalpha():
    print("Username cannot contain numbers")
else:
    print(f"Welcome {userName}!")