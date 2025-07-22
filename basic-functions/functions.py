
# def HappyBirthday(name, age):
#     print(f"Happy Birthday to you {name} you are {age}!")

# HappyBirthday("Dane", 26)
# HappyBirthday("Dane", 26)
# HappyBirthday("Dane", 26)

def display_invoice():
    user_name = input("What's the username for the account: ")
    amount = float(input(f"Enter the amount that {user_name} owes: "))
    due_date = input("Enter the due date: ")
    print(f"{user_name} owes the amount ${amount} and it's due on {due_date}")

add_more = True

while add_more:
    again = input("Enter an invoice ('no' to quit)? ")
    if again.lower() == 'no':
        add_more = False
    else:
        display_invoice()
