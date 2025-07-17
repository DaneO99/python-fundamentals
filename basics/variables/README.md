# Variables

This exercise demonstrates the basic data types in Python and how to work with variables.

## 📚 What You'll Learn

- Different data types in Python
- How to declare and assign variables
- String formatting with f-strings
- Basic conditional statements with boolean variables

## 🔤 Data Types Covered

### 1. Strings
```python
first_name = "Dane Fitzgerald"
food = "pizza"
email = "dane.fitzgerald00@gmail.com"
```
- Used to store text data
- Enclosed in quotes (single or double)
- Can contain letters, numbers, and special characters

### 2. Integers
```python
age = 26
graduation = 2025
```
- Used to store whole numbers
- No decimal points
- Can be positive or negative

### 3. Floats
```python
gpa = 3.2
```
- Used to store decimal numbers
- Also called "floating-point numbers"
- More precise than integers for mathematical calculations

### 4. Booleans
```python
is_student = True
```
- Used to store True or False values
- Useful for conditions and logical operations
- Case-sensitive (True/False, not true/false)

## 🖨️ String Formatting

The code demonstrates f-string formatting (formatted string literals):
```python
print(f"Hello {first_name}")
print(f"My favorite food is {food}")
print(f"My email is {email}")
```

F-strings allow you to embed variables directly into strings using curly braces `{}`.

## 🔄 Conditional Logic

The code includes a basic if-else statement:
```python
if is_student:
    print("I am currently a student")
else:
    print("I am no currently a student")
```

This demonstrates how boolean variables can control program flow.

## 🚀 How to Run

1. Navigate to this folder:
   ```bash
   cd variables
   ```

2. Run the Python file:
   ```bash
   python3 variables.py
   ```

3. **Try this**: Uncomment the print statements (remove the `#`) to see the output!

## 💡 Try It Yourself

1. Change the variable values to your own information
2. Add new variables with different data types
3. Create your own f-string print statements
4. Experiment with different boolean conditions

## 🔗 Next Steps

After mastering variables, move on to:
- [Typecasting](../typecasting/) - Converting between data types
- [User Input](../user-input/) - Getting data from users
- [Arithmetic](../arithmetic/) - Mathematical operations with variables
