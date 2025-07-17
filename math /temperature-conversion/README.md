# Temperature Conversion

This exercise demonstrates how to convert temperatures between Celsius and Fahrenheit using mathematical formulas and conditional logic.

## 📚 What You'll Learn

- Temperature conversion formulas
- Using mathematical operations in real-world applications
- Input validation and case handling
- Rounding numbers for better display
- Practical problem-solving with programming

## 🌡️ How It Works

The program:
1. Asks the user for the temperature unit (C or F)
2. Gets the current temperature value
3. Converts to the opposite unit using the appropriate formula
4. Displays the converted temperature

## 🎯 Code Breakdown

```python
unit = input("What unit do you want to use (F or C) ")
temp = float(input("Okay and what is the current temp in your area "))

if unit == 'C' or unit == 'c':
    temp = round((9 * temp) / 5 + 32, 2)
    print(f"The temp in your area in farenheit is {temp}")
elif unit == "f" or unit == "F":
    temp = round((temp - 32 ) * 5 / 9, 2)
    print(f"The temp in your are in celcius is {temp}")
else:
    print("Invalid unit")
```

## 🔧 Conversion Formulas

### Celsius to Fahrenheit
```python
fahrenheit = (celsius * 9/5) + 32
```
**Example**: 0°C = 32°F, 100°C = 212°F

### Fahrenheit to Celsius
```python
celsius = (fahrenheit - 32) * 5/9
```
**Example**: 32°F = 0°C, 212°F = 100°C

## 📊 Key Features

### Case Insensitive Input
The program accepts both uppercase and lowercase letters:
- `'C'` or `'c'` for Celsius
- `'F'` or `'f'` for Fahrenheit

### Rounding
Uses `round()` function to display results with 2 decimal places:
```python
temp = round((9 * temp) / 5 + 32, 2)
```

### Input Validation
Provides error message for invalid units

## 🚀 How to Run

1. Navigate to this folder:
   ```bash
   cd temperature-conversion
   ```

2. Run the Python file:
   ```bash
   python3 temperature-conversion.py
   ```

3. **Follow the prompts**:
   ```
   What unit do you want to use (F or C) C
   Okay and what is the current temp in your area 25
   The temp in your area in farenheit is 77.0
   ```

## 💡 Try It Yourself

1. **Test common temperatures**:
   - 0°C should equal 32°F
   - 100°C should equal 212°F
   - 68°F should equal 20°C

2. **Test edge cases**:
   - Negative temperatures
   - Very high temperatures
   - Invalid unit inputs

3. **Enhance the program**:
   ```python
   # Add Kelvin conversion
   elif unit.upper() == 'K':
       if temp >= 0:  # Kelvin can't be negative
           celsius = temp - 273.15
           fahrenheit = (celsius * 9/5) + 32
           print(f"Temperature in Celsius: {celsius}")
           print(f"Temperature in Fahrenheit: {fahrenheit}")
       else:
           print("Kelvin cannot be negative!")
   
   # Add temperature descriptions
   if unit.upper() == 'C':
       fahrenheit = round((9 * temp) / 5 + 32, 2)
       if fahrenheit > 100:
           description = "Very hot!"
       elif fahrenheit > 80:
           description = "Hot"
       elif fahrenheit > 60:
           description = "Warm"
       elif fahrenheit > 40:
           description = "Cool"
       else:
           description = "Cold"
       print(f"The temp in fahrenheit is {fahrenheit} ({description})")
   ```

## ⚠️ Common Issues

### Invalid Input Handling
```python
# Current code doesn't handle non-numeric temperature input
# Better approach:
try:
    temp = float(input("Enter temperature: "))
except ValueError:
    print("Please enter a valid number!")
```

### Absolute Zero Validation
```python
# Add validation for physically impossible temperatures
if unit.upper() == 'C' and temp < -273.15:
    print("Temperature cannot be below absolute zero (-273.15°C)")
elif unit.upper() == 'F' and temp < -459.67:
    print("Temperature cannot be below absolute zero (-459.67°F)")
```

## 🔍 Key Concepts Demonstrated

1. **Mathematical Formulas**: Converting between temperature scales
2. **Conditional Logic**: Different operations based on user input
3. **Case Handling**: Accepting both uppercase and lowercase
4. **Number Rounding**: Displaying clean results
5. **User Input**: Getting and processing user data
6. **String Comparison**: Multiple condition checking with `or`

## 🌡️ Temperature Reference

| Description | Celsius | Fahrenheit |
|-------------|---------|------------|
| Absolute Zero | -273.15°C | -459.67°F |
| Water Freezes | 0°C | 32°F |
| Room Temperature | 20°C | 68°F |
| Body Temperature | 37°C | 98.6°F |
| Water Boils | 100°C | 212°F |

## 🔗 Next Steps

After mastering temperature conversion, try:
- [Weight Conversion](../weight%20conversion/) - Practice with different conversion formulas
- [Calculator](../calculator/) - Build more complex calculation programs
- [Mad Libs](../madlibs/) - Apply string manipulation and user input
