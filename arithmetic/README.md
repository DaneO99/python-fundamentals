# Arithmetic

This exercise demonstrates basic arithmetic operations in Python. You'll learn about arithmetic operators and some built-in mathematical functions.

## 📚 What You'll Learn

- Basic arithmetic operations using operators
- Compound assignments for concise code
- Using the math module for complex mathematical tasks
- Understanding order of operations

## ➗ Basic Arithmetic Operators

- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`
- Exponentiation: `**`
- Modulus (remainder): `%`

### 🔍 Example Code

#### Incrementing and Decrementing

```python
friends = 2
friends += 1  # Increment
print(friends)

friends -= 1  # Decrement
print(friends)
```

#### Other Operations

```python
friends *= 8 # Multiplication
print(friends)

friends /= 4 # Division
print(friends)

friends **= 2 # Exponentiation
print(friends)

friends %= 3 # Modulus
print(friends)
```

## 🔢 The Math Module

Python's `math` module provides many useful mathematical functions.

### Key Functions

- `math.pi` and `math.e`: Mathematical constants
- `math.sqrt()`: Square root
- `math.ceil()`: Ceiling (rounding up)
- `math.floor()`: Floor (rounding down)

### 🔍 Example Code

```python
import math

x = 144
y = 7.2
z = 7.9

print(math.pi)
print(math.e)
print(math.sqrt(x))
print(math.ceil(y))
print(math.floor(z))
```

## 📊 Applications

- Calculating area and circumference using `math.pi`
- Rounding numbers for consistent display
- Finding square roots without manual calculation

## 🚀 How to Run

1. Navigate to this folder:
   ```bash
   cd arithmetic
   ```

2. Run any Python file:
   ```bash
   python3 basic.py
   ```

3. **Expected Output**: Based on operations performed

## 💡 Try It Yourself

1. **Modify Arithmetic**: Add new operations or change existing ones
2. **Use math functions in real problems**: Try calculating the area of a circle
3. **Explore more functions**: Experiment with `math.log()`, `math.sin()`, `math.cos()`

Example to calculate area of a circle:
```python
radius = 5
area = math.pi * (radius ** 2)
print(f"Area of circle: {area}")
```

## ⚠️ Common Mistakes

### Forgetting Order of Operations

Commonly called "PEMDAS": parentheses, exponents, multiplication, division, addition, subtraction.

Example:
```python
result = 2 + 3 * 4  # Unintuitive result: 14
```
Use parentheses for clarity:
```python
result = (2 + 3) * 4  # Expected result: 20
```

## 🔗 Next Steps

After mastering arithmetic, move on to:
- [If Statements](../ifstatements/) - Building logic with comparisons
- [Calculator](../calculator/) - Apply arithmetic in a real project

