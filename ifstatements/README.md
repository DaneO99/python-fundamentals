# If Statements

This exercise demonstrates conditional logic in Python using if, elif, and else statements to make decisions in your programs.

## 📚 What You'll Learn

- Basic if/else statement structure
- Using elif for multiple conditions
- Comparison operators
- Logical operators (and, or, not)
- Boolean logic in conditional statements

## 🔄 Conditional Logic Structure

### Basic If/Else
```python
if condition:
    # Code runs if condition is True
else:
    # Code runs if condition is False
```

### If/Elif/Else
```python
if condition1:
    # Code runs if condition1 is True
elif condition2:
    # Code runs if condition2 is True
else:
    # Code runs if no conditions are True
```

## 🎯 Code Examples

### 1. Age Check (Commented)
```python
age = int(input("What is your age?: "))

if age >= 22:
    print(f"Congrats at the age of {age} you can buy alcohol.")
elif age == 21:
    print(f"Congrats on being {age} you can buy alcohol now.")
else:
    print(f"Sorry at the age of {age} you can't buy alcohol.")
```

### 2. Food Response Check (Commented)
```python
response = input("Would you like food? ")

if response == 'Y' or response == "Yes" or response == "yes" or response == 'y':
    print("Okay here is some food")
else:
    print("Okay you are not hungry right now.")
```

### 3. Name Validation (Commented)
```python
name = input("Enter your name. ")

if name == "":
    print("You did not type in your name. ")
else:
    print(f"Hello {name}")
```

### 4. Boolean Check (Active)
```python
for_sale = False

if for_sale:
    print("This item is for sale.")
else:
    print("This item is not for sale.")
```

## 🔧 Comparison Operators

- `==` Equal to
- `!=` Not equal to
- `>` Greater than
- `<` Less than
- `>=` Greater than or equal to
- `<=` Less than or equal to

## 🔗 Logical Operators

- `and` Both conditions must be True
- `or` At least one condition must be True
- `not` Reverses the boolean value

### Examples:
```python
# AND operator
if age >= 18 and age <= 65:
    print("You are of working age")

# OR operator
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")

# NOT operator
if not is_raining:
    print("Great weather for a walk!")
```

## 🚀 How to Run

1. Navigate to this folder:
   ```bash
   cd ifstatements
   ```

2. Run the Python file:
   ```bash
   python3 if.py
   ```

3. **Expected Output**: `This item is not for sale.`

## 💡 Try It Yourself

1. **Uncomment examples**: Remove `#` from different sections to test them
2. **Create your own conditions**: Try these examples:
   ```python
   # Grade checker
   score = int(input("Enter your score: "))
   if score >= 90:
       print("Grade: A")
   elif score >= 80:
       print("Grade: B")
   elif score >= 70:
       print("Grade: C")
   else:
       print("Grade: F")
   
   # Weather advisor
   temperature = float(input("Temperature: "))
   if temperature > 80:
       print("It's hot! Wear shorts.")
   elif temperature > 60:
       print("Nice weather! Wear a t-shirt.")
   else:
       print("It's cold! Wear a jacket.")
   ```

3. **Practice with different data types**: Try conditions with strings, numbers, and booleans

## ⚠️ Common Mistakes

### 1. Using = instead of ==
```python
# Wrong - this assigns a value
if age = 18:
    print("You're 18")

# Correct - this compares values
if age == 18:
    print("You're 18")
```

### 2. Not handling case sensitivity
```python
# This might miss valid responses
if response == "yes":
    print("Yes selected")

# Better approach
if response.lower() == "yes":
    print("Yes selected")
```

### 3. Forgetting indentation
```python
# Wrong - no indentation
if age >= 18:
print("You're an adult")

# Correct - proper indentation
if age >= 18:
    print("You're an adult")
```

## 🔗 Next Steps

After mastering if statements, move on to:
- [Logic Operators](../logicoperators/) - More complex boolean logic
- [Calculator](../calculator/) - Apply conditionals in a real project
- [Temperature Conversion](../temperature-conversion/) - Use conditionals for validation
