
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for rows in range(rows):
    for columns in range(1,columns + 1):
        print(symbol, end=" ")
    print()