# Conditionals (Ternary Operators)

This exercise demonstrates conditional expressions, also known as ternary operators, which provide a concise way to write simple if-else statements.

## 📚 What You'll Learn

- Ternary operator syntax and usage
- Writing concise conditional expressions
- Comparing ternary vs traditional if-else
- Variable assignment with conditions
- Practical applications of conditional expressions

## 🎯 Code Examples

```python
num = 1
a = 7
b = 4
age = 21

print("Positive" if num > 0 else "Negative")
print("Even" if num % 2 == 0 else "Odd")

max_num = a if a > b else b
min_num = a if a < b else b

print(max_num)
print(min_num)

status = "Adult" if age >= 18 else "Child"
print(status)
```

## 🔧 Ternary Operator Syntax

### Basic Structure
```python
value_if_true if condition else value_if_false
```

### Traditional vs Ternary
```python
# Traditional if-else
if score >= 60:
    grade = "Pass"
else:
    grade = "Fail"

# Ternary operator
grade = "Pass" if score >= 60 else "Fail"
```

## 🚀 How to Run

1. Navigate to this folder:
   ```bash
   cd "logic /conditionals"
   ```

2. Run the Python file:
   ```bash
   python3 conditionals.py
   ```

3. **Expected Output**:
   ```
   Positive
   Odd
   7
   4
   Adult
   ```

## 💡 Try It Yourself

1. **Basic examples**:
   ```python
   # Temperature check
   temp = 75
   weather = "Hot" if temp > 80 else "Cold" if temp < 60 else "Comfortable"
   print(weather)  # "Comfortable"
   
   # Sign check
   number = -5
   sign = "Positive" if number > 0 else "Negative" if number < 0 else "Zero"
   print(sign)  # "Negative"
   
   # Grade calculation
   score = 85
   letter_grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
   print(letter_grade)  # "B"
   ```

2. **Practical applications**:
   ```python
   # File size formatting
   size_bytes = 1024
   size_display = f"{size_bytes} bytes" if size_bytes < 1024 else f"{size_bytes/1024:.1f} KB"
   
   # Pluralization
   item_count = 5
   message = f"You have {item_count} item" + ("" if item_count == 1 else "s")
   
   # Price calculation
   quantity = 10
   price_per_item = 5.00
   discount = 0.1 if quantity >= 10 else 0.05 if quantity >= 5 else 0
   total = quantity * price_per_item * (1 - discount)
   ```

3. **Boolean operations**:
   ```python
   # Login validation
   username = "admin"
   password = "secret"
   is_logged_in = True if username == "admin" and password == "secret" else False
   
   # Permission check
   user_role = "admin"
   can_delete = True if user_role in ["admin", "moderator"] else False
   
   # Age verification
   age = 25
   can_vote = True if age >= 18 else False
   can_drink = True if age >= 21 else False
   ```

## 🔍 Advanced Usage

### Nested Conditionals
```python
# Nested ternary operators
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"

# More readable version
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
```

### Function Calls in Conditionals
```python
def get_discount(customer_type):
    return 0.2 if customer_type == "premium" else 0.1 if customer_type == "member" else 0

# Usage
customer = "premium"
discount = get_discount(customer)
```

### List/Dictionary Access
```python
# Safe dictionary access
user_data = {"name": "John", "age": 30}
display_name = user_data["name"] if "name" in user_data else "Unknown"

# List element access
numbers = [1, 2, 3]
first_element = numbers[0] if numbers else None
```

## 🎯 When to Use Ternary Operators

### ✅ Good Use Cases
- Simple variable assignment based on condition
- Short, readable conditions
- Return values from functions
- Default value assignment

### ❌ Avoid When
- Complex nested conditions (hard to read)
- Multiple statements needed
- Complex logic that's better as full if-else

## 🔍 Comparison Examples

### Temperature Status
```python
# Traditional approach
temperature = 75
if temperature > 80:
    status = "Hot"
elif temperature > 60:
    status = "Warm"
else:
    status = "Cold"

# Ternary approach
status = "Hot" if temperature > 80 else "Warm" if temperature > 60 else "Cold"
```

### User Access Level
```python
# Traditional approach
user_age = 25
if user_age >= 18:
    access_level = "Full Access"
else:
    access_level = "Limited Access"

# Ternary approach
access_level = "Full Access" if user_age >= 18 else "Limited Access"
```

## ⚠️ Common Mistakes

### 1. Overusing Nested Ternary
```python
# Hard to read
result = "A" if x > 90 else "B" if x > 80 else "C" if x > 70 else "D" if x > 60 else "F"

# Better approach
def get_grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else: return "F"
```

### 2. Forgetting Parentheses
```python
# Might not work as expected
result = "Pass" if score >= 60 else "Fail" if score >= 0 else "Invalid"

# Clearer with parentheses
result = ("Pass" if score >= 60 else "Fail") if score >= 0 else "Invalid"
```

### 3. Complex Conditions
```python
# Too complex for ternary
result = "Valid" if len(password) >= 8 and any(c.isupper() for c in password) and any(c.islower() for c in password) else "Invalid"

# Better as traditional if-else
if len(password) >= 8 and any(c.isupper() for c in password) and any(c.islower() for c in password):
    result = "Valid"
else:
    result = "Invalid"
```

## 🎯 Real-World Applications

### Web Development
```python
# Status message
status_code = 200
message = "Success" if status_code == 200 else "Not Found" if status_code == 404 else "Error"

# User role display
user_role = "admin"
nav_items = ["Dashboard", "Users", "Settings"] if user_role == "admin" else ["Dashboard", "Profile"]
```

### Data Processing
```python
# Data validation
data_point = 95
category = "High" if data_point > 80 else "Medium" if data_point > 40 else "Low"

# File processing
file_extension = ".txt"
file_type = "Text" if file_extension == ".txt" else "Image" if file_extension in [".jpg", ".png"] else "Unknown"
```

## 🔗 Next Steps

After mastering conditionals, explore:
- [Logic Operators](../logicoperators/) - Combine multiple conditions
- [Loops](../../loops/) - Use conditionals in iterative structures
- [Functions](../../functions/) - Create reusable conditional logic

Conditional expressions are powerful tools for writing clean, readable code when used appropriately!
