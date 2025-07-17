# Weight Conversion

This exercise demonstrates how to convert weight between pounds and kilograms using mathematical operations and conditional logic.

## 📚 What You'll Learn

- Weight conversion formulas
- Using division and multiplication for unit conversion
- String comparison for multiple valid inputs
- Practical applications of mathematical operations
- Input validation and user-friendly output

## ⚖️ How It Works

The program:
1. Gets the weight value from the user
2. Asks for the current unit (pounds or kilograms)
3. Converts to the opposite unit using the conversion factor
4. Displays the converted weight with proper rounding

## 🎯 Code Breakdown

```python
weight = float(input("Enter your weight "))
unit = input("Is this unit it pounds(lbs) or kilograms(kgs) ")

if unit == "lbs" or unit == "pounds":
    weight /= 2.205
    print(f"You weigh {round(weight , 2)} in kgs")
elif unit == "kgs" or unit == "kilograms":
    weight *= 2.205
    print(f"You weigh {round(weight, 2)} in pounds ")
else:
    print("Invalid unit")
```

## 🔧 Conversion Formulas

### Pounds to Kilograms
```python
kilograms = pounds / 2.205
```
**Example**: 220 lbs ≈ 99.77 kg

### Kilograms to Pounds
```python
pounds = kilograms * 2.205
```
**Example**: 70 kg ≈ 154.35 lbs

## 📊 Key Features

### Multiple Input Formats
The program accepts various input formats:
- `"lbs"` or `"pounds"` for pounds
- `"kgs"` or `"kilograms"` for kilograms

### Precise Rounding
Uses `round()` function to display results with 2 decimal places for readability

### Input Validation
Provides error message for invalid units

## 🚀 How to Run

1. Navigate to this folder:
   ```bash
   cd "weight conversion"
   ```

2. Run the Python file:
   ```bash
   python3 weight-conversion.py
   ```

3. **Follow the prompts**:
   ```
   Enter your weight 150
   Is this unit it pounds(lbs) or kilograms(kgs) lbs
   You weigh 68.03 in kgs
   ```

## 💡 Try It Yourself

1. **Test common weights**:
   - 100 lbs should equal ~45.35 kg
   - 50 kg should equal ~110.23 lbs
   - 200 lbs should equal ~90.70 kg

2. **Test different input formats**:
   - Try "pounds" vs "lbs"
   - Try "kilograms" vs "kgs"
   - Test invalid inputs

3. **Enhance the program**:
   ```python
   # Add case insensitive input
   unit = unit.lower()
   
   # Add more weight units
   elif unit in ["oz", "ounces"]:
       # Convert ounces to pounds first, then to kg
       weight_lbs = weight / 16
       weight_kg = weight_lbs / 2.205
       print(f"You weigh {round(weight_kg, 2)} kg")
   
   # Add weight categories
   if unit in ["lbs", "pounds"]:
       weight_kg = weight / 2.205
       if weight_kg < 18.5 * (1.7**2):  # Assuming average height
           category = "underweight"
       elif weight_kg < 25 * (1.7**2):
           category = "normal weight"
       else:
           category = "overweight"
       print(f"You weigh {round(weight_kg, 2)} kg ({category})")
   ```

## ⚠️ Common Issues

### Conversion Factor Precision
The current code uses 2.205 as the conversion factor:
```python
# More precise conversion factor
POUNDS_TO_KG = 0.45359237
KG_TO_POUNDS = 2.20462262185

# Better approach:
if unit == "lbs" or unit == "pounds":
    weight_kg = weight * POUNDS_TO_KG
    print(f"You weigh {round(weight_kg, 2)} kg")
```

### Invalid Input Handling
```python
# Better error handling
try:
    weight = float(input("Enter your weight: "))
    if weight <= 0:
        print("Weight must be positive!")
except ValueError:
    print("Please enter a valid number!")
```

### Case Sensitivity
```python
# Make input case insensitive
unit = input("Unit (lbs/pounds or kg/kilograms): ").lower()
```

## 🔍 Key Concepts Demonstrated

1. **Mathematical Operations**: Division and multiplication for conversion
2. **Conditional Logic**: Different operations based on input
3. **Multiple Conditions**: Using `or` for alternative valid inputs
4. **Number Rounding**: Displaying clean results
5. **User Input**: Getting and processing user data
6. **String Comparison**: Checking against multiple valid strings

## ⚖️ Weight Reference

| Description | Pounds | Kilograms |
|-------------|---------|-----------|
| Newborn baby | ~7 lbs | ~3.2 kg |
| Small dog | ~20 lbs | ~9 kg |
| Medium dog | ~50 lbs | ~23 kg |
| Average adult | ~150 lbs | ~68 kg |
| Large dog | ~100 lbs | ~45 kg |

## 🔗 Next Steps

After mastering weight conversion, try:
- [Mad Libs](../madlibs/) - Apply string manipulation and user input
- [Calculator](../calculator/) - Build more complex calculation programs
- [Temperature Conversion](../temperature-conversion/) - Practice with different conversion formulas
