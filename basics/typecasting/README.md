# Typecasting

This exercise demonstrates how to convert between different data types in Python, also known as type conversion or typecasting.

## 📚 What You'll Learn

- How to convert between different data types
- The difference between explicit and implicit type conversion
- When and why you might need to convert data types
- Common typecasting functions in Python

## 🔄 Type Conversion Example

The code shows a practical example of converting a float to an integer:

```python
name = "Dane Fitzgerald"
age = 25
gpa = 2.9
is_student = True

gpa = int(gpa)  # Convert float 2.9 to integer 2

print(gpa)  # Output: 2
```

## 🛠️ Common Typecasting Functions

### 1. `int()` - Convert to Integer
```python
float_number = 3.14
integer_number = int(float_number)  # Result: 3
```
- Truncates decimal part (doesn't round)
- Can convert strings containing numbers: `int("42")` → `42`

### 2. `float()` - Convert to Float
```python
integer_number = 42
float_number = float(integer_number)  # Result: 42.0
```
- Adds decimal point to integers
- Can convert strings: `float("3.14")` → `3.14`

### 3. `str()` - Convert to String
```python
number = 42
text = str(number)  # Result: "42"
```
- Converts any data type to string representation
- Useful for concatenation and display

### 4. `bool()` - Convert to Boolean
```python
number = 0
boolean_value = bool(number)  # Result: False
```
- `0`, `0.0`, `""`, `[]`, `{}`, `None` → `False`
- Everything else → `True`

## ⚠️ Important Notes

### Precision Loss
When converting from float to int, you lose the decimal part:
```python
original = 2.9
converted = int(original)  # 2 (not 3!)
```

### Error Handling
Some conversions can cause errors:
```python
# This would cause an error:
# int("hello")  # ValueError: invalid literal
```

## 🚀 How to Run

1. Navigate to this folder:
   ```bash
   cd typecasting
   ```

2. Run the Python file:
   ```bash
   python3 typecasting.py
   ```

3. **Expected Output**: `2`

## 💡 Try It Yourself

1. Try converting the other variables to different types
2. Experiment with converting strings to numbers
3. See what happens when you convert numbers to booleans
4. Try these examples:
   ```python
   # String to number
   age_str = "25"
   age_num = int(age_str)
   
   # Number to string
   score = 95.5
   score_str = str(score)
   
   # Boolean conversions
   print(bool(0))    # False
   print(bool(1))    # True
   print(bool(""))   # False
   print(bool("Hi")) # True
   ```

## 🔗 Next Steps

After understanding typecasting, move on to:
- [User Input](../user-input/) - Getting and converting user input
- [Arithmetic](../arithmetic/) - Mathematical operations with different types
- [Calculator](../calculator/) - Apply typecasting in a real project
