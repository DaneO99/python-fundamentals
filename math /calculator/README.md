# Calculator

This exercise demonstrates how to build a simple calculator that performs basic arithmetic operations based on user input.

## 📚 What You'll Learn

- Combining user input with conditional logic
- Building interactive programs
- Input validation and error handling
- Practical application of arithmetic operations

## 🧮 How It Works

The calculator follows this process:
1. Gets two numbers from the user
2. Asks which operation to perform
3. Uses if/elif statements to determine the operation
4. Performs the calculation and displays the result

## 🎯 Code Breakdown

```python
import math

# Get user input
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

# Get operation choice
response = input("What do you want to do + , - , / , * : ")

# Perform calculation based on user choice
if response == "+":
    print(x + y)
elif response == "-":
    print(x - y)
elif response == "/":
    print(x / y)
elif response == "*":
    print(x * y)
else:
    print("Invalid response.")
```

## 🔧 Features

### Supported Operations
- **Addition (+)**: Adds two numbers
- **Subtraction (-)**: Subtracts the second number from the first
- **Division (/)**: Divides the first number by the second
- **Multiplication (*)**: Multiplies two numbers

### Input Validation
- Uses `float()` to handle decimal numbers
- Provides error message for invalid operations
- Handles both integers and decimal numbers

## 🚀 How to Run

1. Navigate to this folder:
   ```bash
   cd calculator
   ```

2. Run the Python file:
   ```bash
   python3 calculator.py
   ```

3. **Follow the prompts**:
   ```
   Enter the first number: 10
   Enter the second number: 5
   What do you want to do + , - , / , * : +
   15.0
   ```

## 💡 Try It Yourself

1. **Test different operations**: Try all four operations with various numbers
2. **Test edge cases**: What happens with division by zero?
3. **Enhance the calculator**: Add these features:
   ```python
   # Add exponentiation
   elif response == "**":
       print(x ** y)
   
   # Add modulus
   elif response == "%":
       print(x % y)
   
   # Add square root (for first number only)
   elif response == "sqrt":
       print(math.sqrt(x))
   ```

4. **Improve user experience**: Make the output more descriptive:
   ```python
   if response == "+":
       print(f"{x} + {y} = {x + y}")
   ```

## ⚠️ Potential Issues

### Division by Zero
```python
# Current code doesn't handle this:
# 10 / 0  # This will cause an error

# Better approach:
elif response == "/":
    if y != 0:
        print(x / y)
    else:
        print("Error: Cannot divide by zero!")
```

### Invalid Number Input
```python
# What if user enters non-numeric input?
# float("hello")  # This will cause an error

# Better approach (advanced):
try:
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
except ValueError:
    print("Please enter valid numbers!")
```

## 🔍 Key Concepts Demonstrated

1. **User Input**: Getting and converting user input
2. **Conditional Logic**: Using if/elif/else for decision making
3. **Arithmetic Operations**: Performing calculations
4. **Error Handling**: Basic validation with else clause
5. **Module Usage**: Importing math module (though not used in current code)

## 🚀 Enhancement Ideas

1. **Loop for multiple calculations**
2. **Memory functions** (store/recall results)
3. **More advanced operations** (sin, cos, log, etc.)
4. **Better error handling**
5. **GUI interface** using tkinter

## 🔗 Next Steps

After building the calculator, try:
- [Temperature Conversion](../temperature-conversion/) - Another practical application
- [Weight Conversion](../weight%20conversion/) - More conversion practice
- [Mad Libs](../madlibs/) - Apply string manipulation and user input
