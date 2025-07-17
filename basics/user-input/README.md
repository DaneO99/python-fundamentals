# User Input

This exercise demonstrates how to get input from users and use it in your Python programs.

## 📚 What You'll Learn

- How to use the `input()` function to get user input
- Converting user input to different data types
- Creating interactive programs
- Practical applications of user input

## 🎯 Code Examples

The file contains several examples, with the Shopping Cart Program currently active:

### 1. Basic Name Input (Commented)
```python
name = input("What is your name? ")
print(f"Hello {name}")
```

### 2. Age Input with Math (Commented)
```python
age = int(input("How old are you? "))
print(f"You are {age}")
age += 1
print(f"Happy Birthday. You are now {age}")
```

### 3. Rectangle Area Calculator (Commented)
```python
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is {area} cm²")
```

### 4. Shopping Cart Program (Active)
```python
item = input("What item would you like to buy? ")
price = float(input("How much is it? "))
quantity = float(input("How many do you want to buy? "))
total = price * quantity
print(f"The {item} in the quantity of {quantity} is ${total}")
```

## 🔧 Key Concepts

### The `input()` Function
- Always returns a string, even if the user enters numbers
- Takes a prompt message as an argument
- Waits for the user to press Enter

### Type Conversion with Input
Since `input()` returns strings, you often need to convert:
```python
# For integers
age = int(input("Your age: "))

# For floats
price = float(input("Price: "))

# For strings (no conversion needed)
name = input("Your name: ")
```

### Interactive Programs
User input makes programs interactive and dynamic:
- Programs can respond to user choices
- Each run can produce different results
- Users feel more engaged

## 🚀 How to Run

1. Navigate to this folder:
   ```bash
   cd user-input
   ```

2. Run the Python file:
   ```bash
   python3 user_input.py
   ```

3. **Follow the prompts** and enter your responses

### Expected Interaction:
```
What item would you like to buy? apple
How much is it? 1.50
How many do you want to buy? 5
The apple in the quantity of 5.0 is $7.5
```

## 💡 Try It Yourself

1. **Uncomment other examples**: Remove the `#` from different sections to try them
2. **Create your own input program**: Try these ideas:
   ```python
   # Personal information collector
   name = input("Name: ")
   city = input("City: ")
   hobby = input("Hobby: ")
   print(f"Hi {name} from {city}! I love {hobby} too!")
   
   # Simple calculator
   num1 = float(input("First number: "))
   num2 = float(input("Second number: "))
   result = num1 + num2
   print(f"Sum: {result}")
   ```

3. **Handle different data types**: Practice converting input to int, float, and keeping as string

## ⚠️ Common Mistakes

### 1. Forgetting Type Conversion
```python
# Wrong - this will cause an error
age = input("Age: ")  # This is a string!
next_year = age + 1   # Can't add number to string

# Correct
age = int(input("Age: "))
next_year = age + 1
```

### 2. Not Handling Invalid Input
```python
# This could crash if user enters non-numeric text
age = int(input("Age: "))

# Better approach (advanced):
try:
    age = int(input("Age: "))
except ValueError:
    print("Please enter a valid number")
```

## 🔗 Next Steps

After mastering user input, move on to:
- [Arithmetic](../arithmetic/) - Mathematical operations with user input
- [If Statements](../ifstatements/) - Making decisions based on user input
- [Calculator](../calculator/) - Build an interactive calculator
