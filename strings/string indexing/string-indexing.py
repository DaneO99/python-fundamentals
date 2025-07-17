
credit_number = "1234-5678-9012-3456"

# print(credit_number[0])
# print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-1])
# print(credit_number[0::+1])

last_four = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_four}")

reverse_number = credit_number[::-1]
print(f"{reverse_number}")
