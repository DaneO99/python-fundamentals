# Format Specifiers

This exercise demonstrates advanced string formatting techniques in Python using format specifiers to control how values are displayed.

## 📚 What You'll Learn

- Advanced f-string formatting
- Alignment and padding options
- Number formatting and precision
- Width and fill characters
- Professional output formatting

## 🎯 Code Example

```python
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price one is {price1:>10}")
print(f"Price two is {price2:<10}")
print(f"Price three is {price3:010}")
```

## 🔧 Format Specifier Syntax

The general format is: `{value:format_spec}`

### Basic Structure
```
{value:[fill][align][sign][#][0][width][,][.precision][type]}
```

## 📐 Alignment Options

### Right Alignment (>)
```python
value = 42
print(f"{value:>10}")  # "        42"
```

### Left Alignment (<)
```python
value = 42
print(f"{value:<10}")  # "42        "
```

### Center Alignment (^)
```python
value = 42
print(f"{value:^10}")  # "    42    "
```

## 🔢 Number Formatting

### Zero Padding
```python
number = 42
print(f"{number:05}")  # "00042"
print(f"{number:010}") # "0000000042"
```

### Decimal Precision
```python
pi = 3.14159
print(f"{pi:.2f}")   # "3.14"
print(f"{pi:.4f}")   # "3.1416"
```

### Thousands Separator
```python
big_number = 1234567
print(f"{big_number:,}")   # "1,234,567"
print(f"{big_number:_}")   # "1_234_567"
```

## 🚀 How to Run

1. Navigate to this folder:
   ```bash
   cd format-specifiers
   ```

2. Run the Python file:
   ```bash
   python3 specifiers.py
   ```

3. **Expected Output**:
   ```
   Price one is    3.14159
   Price two is -987.65   
   Price three is 0000012.34
   ```

## 💡 Try It Yourself

1. **Test different alignments**:
   ```python
   name = "Python"
   print(f"{name:>15}")  # Right align in 15 characters
   print(f"{name:<15}")  # Left align in 15 characters
   print(f"{name:^15}")  # Center align in 15 characters
   ```

2. **Practice with numbers**:
   ```python
   # Currency formatting
   price = 19.99
   print(f"${price:>8.2f}")  # "$   19.99"
   print(f"${price:<8.2f}")  # "$19.99   "
   
   # Percentage formatting
   rate = 0.1234
   print(f"{rate:.2%}")      # "12.34%"
   
   # Scientific notation
   big_num = 1234567890
   print(f"{big_num:.2e}")   # "1.23e+09"
   ```

3. **Create formatted tables**:
   ```python
   # Product table
   products = [
       ("Apple", 1.25, 10),
       ("Banana", 0.75, 25),
       ("Orange", 1.50, 15)
   ]
   
   print(f"{'Product':<10} {'Price':>8} {'Qty':>5}")
   print("-" * 25)
   for name, price, qty in products:
       print(f"{name:<10} ${price:>7.2f} {qty:>5}")
   ```

## 🎨 Advanced Examples

### Custom Fill Characters
```python
value = 42
print(f"{value:*^10}")  # "****42****"
print(f"{value:0>10}")  # "0000000042"
print(f"{value:-<10}")  # "42--------"
```

### Sign Control
```python
positive = 42
negative = -42
print(f"{positive:+}")   # "+42"
print(f"{negative:+}")   # "-42"
print(f"{positive: }")   # " 42" (space for positive)
```

### Binary/Hex/Octal
```python
number = 255
print(f"{number:b}")     # "11111111" (binary)
print(f"{number:o}")     # "377" (octal)
print(f"{number:x}")     # "ff" (hex lowercase)
print(f"{number:X}")     # "FF" (hex uppercase)
```

## 📊 Practical Applications

### 1. Financial Reports
```python
def format_currency(amount):
    return f"${amount:>10,.2f}"

print("Monthly Report:")
print(format_currency(1234.56))   # "$  1,234.56"
print(format_currency(123456.78)) # "$123,456.78"
```

### 2. Progress Bars
```python
def progress_bar(percent):
    filled = int(percent * 20)
    bar = "█" * filled + "░" * (20 - filled)
    return f"{bar} {percent:.1%}"

print(progress_bar(0.75))  # "███████████████░░░░░ 75.0%"
```

### 3. Data Tables
```python
def format_table_row(name, value, percent):
    return f"{name:<15} {value:>8.2f} {percent:>6.1%}"

print(format_table_row("Revenue", 12345.67, 0.156))
# "Revenue          12345.67  15.6%"
```

## 🔍 Key Concepts

1. **Alignment**: Control text positioning within fields
2. **Padding**: Add characters to reach desired width
3. **Precision**: Control decimal places for floating-point numbers
4. **Type Conversion**: Format numbers as different representations
5. **Professional Output**: Create well-formatted, readable displays

## ⚠️ Common Patterns

### Date/Time Formatting
```python
from datetime import datetime
now = datetime.now()
print(f"{now:%Y-%m-%d %H:%M:%S}")  # "2023-07-15 14:30:45"
```

### Conditional Formatting
```python
def format_grade(score):
    if score >= 90:
        return f"{score:>6.1f}% A"
    elif score >= 80:
        return f"{score:>6.1f}% B"
    else:
        return f"{score:>6.1f}% F"
```

## 🔗 Next Steps

After mastering format specifiers, explore:
- [Loops](../loops/) - Use formatting in iterative output
- [Functions](../functions/) - Create reusable formatting functions (when added)
- [File I/O](../file-io/) - Format data for file output (when added)
- [Data Structures](../data-structures/) - Format complex data (when added)

Format specifiers are essential for creating professional, readable output in your Python programs!
