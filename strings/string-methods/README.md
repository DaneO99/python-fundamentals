# String Methods

This exercise demonstrates built-in string methods for validation, transformation, and analysis using a username validation example.

## 📚 What You'll Learn

- Built-in string methods for text analysis
- Input validation using string methods
- String searching and checking functions
- Creating robust user input systems
- Text processing and validation patterns

## 🎯 Code Example

```python
userName = input("Input a username:")

if len(userName) > 12:
    print("Username is too long")
elif not userName.find(" ") == -1:
    print("Username cannot contain spaces")
elif not userName.isalpha():
    print("Username cannot contain numbers")
else:
    print(f"Welcome {userName}!")
```

## 🔧 Essential String Methods

### Length and Searching
```python
text = "Hello World"
print(len(text))           # 11
print(text.find("World"))  # 6
print(text.find("xyz"))    # -1 (not found)
```

### Character Type Checking
```python
text = "Hello123"
print(text.isalpha())      # False (contains numbers)
print(text.isdigit())      # False (contains letters)
print(text.isalnum())      # True (letters and numbers)
print(text.isspace())      # False (not all whitespace)
```

### Case Conversion
```python
text = "Hello World"
print(text.upper())        # "HELLO WORLD"
print(text.lower())        # "hello world"
print(text.title())        # "Hello World"
print(text.capitalize())   # "Hello world"
```

### String Testing
```python
text = "Hello"
print(text.startswith("He"))  # True
print(text.endswith("lo"))    # True
print(text.isupper())         # False
print(text.islower())         # False
```

## 🚀 How to Run

1. Navigate to this folder:
   ```bash
   cd "strings/string-methods"
   ```

2. Run the Python file:
   ```bash
   python3 string-methods.py
   ```

3. **Test different inputs**:
   ```
   Input a username: john        # "Welcome john!"
   Input a username: verylongusername  # "Username is too long"
   Input a username: john doe    # "Username cannot contain spaces"
   Input a username: john123     # "Username cannot contain numbers"
   ```

## 💡 Try It Yourself

1. **Enhanced username validation**:
   ```python
   def validate_username(username):
       if len(username) < 3:
           return "Username too short (minimum 3 characters)"
       elif len(username) > 12:
           return "Username too long (maximum 12 characters)"
       elif not username.isalnum():
           return "Username can only contain letters and numbers"
       elif username.isdigit():
           return "Username cannot be all numbers"
       elif not username[0].isalpha():
           return "Username must start with a letter"
       else:
           return "Valid username!"
   ```

2. **Email validation**:
   ```python
   def validate_email(email):
       if "@" not in email:
           return "Invalid: Missing @ symbol"
       elif email.count("@") != 1:
           return "Invalid: Multiple @ symbols"
       elif email.startswith("@") or email.endswith("@"):
           return "Invalid: @ cannot be at start or end"
       elif ".." in email:
           return "Invalid: Consecutive dots not allowed"
       else:
           return "Valid email format"
   ```

3. **Password strength checker**:
   ```python
   def check_password_strength(password):
       if len(password) < 8:
           return "Weak: Too short"
       elif password.islower():
           return "Weak: No uppercase letters"
       elif password.isupper():
           return "Weak: No lowercase letters"
       elif password.isalpha():
           return "Medium: No numbers or symbols"
       elif password.isalnum():
           return "Medium: No special characters"
       else:
           return "Strong: Good password!"
   ```

## 🔍 Advanced String Methods

### Whitespace Handling
```python
text = "  Hello World  "
print(text.strip())       # "Hello World"
print(text.lstrip())      # "Hello World  "
print(text.rstrip())      # "  Hello World"
```

### String Replacement
```python
text = "Hello World"
print(text.replace("World", "Python"))  # "Hello Python"
print(text.replace("l", "L"))           # "HeLLo WorLd"
print(text.replace("l", "L", 1))        # "HeLlo World" (replace first only)
```

### String Splitting and Joining
```python
text = "apple,banana,orange"
fruits = text.split(",")              # ["apple", "banana", "orange"]
rejoined = " | ".join(fruits)         # "apple | banana | orange"
```

### String Formatting Methods
```python
text = "hello world"
print(text.center(20, "-"))   # "----hello world-----"
print(text.ljust(15, "."))    # "hello world...."
print(text.rjust(15, "."))    # "....hello world"
print(text.zfill(15))         # "0000hello world"
```

## 📋 Common Validation Patterns

### Phone Number Validation
```python
def validate_phone(phone):
    # Remove common separators
    clean_phone = phone.replace("-", "").replace(" ", "").replace("(", "").replace(")", "")
    
    if not clean_phone.isdigit():
        return "Invalid: Contains non-digit characters"
    elif len(clean_phone) != 10:
        return "Invalid: Must be 10 digits"
    else:
        return "Valid phone number"
```

### Name Validation
```python
def validate_name(name):
    if not name.strip():
        return "Invalid: Name cannot be empty"
    elif any(char.isdigit() for char in name):
        return "Invalid: Name cannot contain numbers"
    elif len(name.strip()) < 2:
        return "Invalid: Name too short"
    else:
        return "Valid name"
```

### Credit Card Validation (Basic)
```python
def validate_credit_card(card):
    # Remove spaces and dashes
    clean_card = card.replace(" ", "").replace("-", "")
    
    if not clean_card.isdigit():
        return "Invalid: Contains non-digit characters"
    elif len(clean_card) < 13 or len(clean_card) > 19:
        return "Invalid: Wrong length"
    else:
        return "Valid format"
```

## 🔍 Method Reference

| Method | Description | Example |
|--------|-------------|---------|
| `len()` | Get string length | `len("hello")` → `5` |
| `find()` | Find substring index | `"hello".find("ll")` → `2` |
| `isalpha()` | Check if all letters | `"hello".isalpha()` → `True` |
| `isdigit()` | Check if all digits | `"123".isdigit()` → `True` |
| `isalnum()` | Check if letters/numbers | `"hello123".isalnum()` → `True` |
| `isspace()` | Check if all whitespace | `"   ".isspace()` → `True` |
| `startswith()` | Check start of string | `"hello".startswith("he")` → `True` |
| `endswith()` | Check end of string | `"hello".endswith("lo")` → `True` |
| `upper()` | Convert to uppercase | `"hello".upper()` → `"HELLO"` |
| `lower()` | Convert to lowercase | `"HELLO".lower()` → `"hello"` |
| `strip()` | Remove whitespace | `" hello ".strip()` → `"hello"` |
| `replace()` | Replace substring | `"hello".replace("l", "x")` → `"hexxo"` |

## ⚠️ Common Pitfalls

### 1. String Immutability
```python
text = "hello"
text.upper()  # This doesn't change text!
print(text)   # Still "hello"

# Correct way:
text = text.upper()
print(text)   # "HELLO"
```

### 2. Case Sensitivity
```python
# Case-sensitive methods
print("Hello".find("hello"))  # -1 (not found)
print("Hello".lower().find("hello"))  # 0 (found)
```

### 3. Empty String Handling
```python
empty = ""
print(empty.isalpha())  # False
print(empty.isdigit())  # False
print(empty.isspace())  # False
print(len(empty))       # 0
```

## 🎯 Real-World Applications

### Form Validation
```python
def validate_form_field(field_name, value, field_type):
    if not value.strip():
        return f"{field_name} cannot be empty"
    
    if field_type == "name":
        if not value.replace(" ", "").isalpha():
            return f"{field_name} can only contain letters"
    elif field_type == "age":
        if not value.isdigit():
            return f"{field_name} must be a number"
    elif field_type == "email":
        if "@" not in value or "." not in value:
            return f"{field_name} must be a valid email"
    
    return "Valid"
```

### Data Cleaning
```python
def clean_data(text):
    # Remove extra whitespace, convert to title case
    return text.strip().title()

def normalize_phone(phone):
    # Remove all non-digit characters
    return ''.join(char for char in phone if char.isdigit())
```

## 🔗 Next Steps

After mastering string methods, explore:
- [Format Specifiers](../../format-specifiers/) - Advanced string formatting
- [Loops](../../loops/) - Iterate through strings for complex processing
- [Regular Expressions](../../regex/) - Pattern matching (when added)

String methods are essential for data validation, cleaning, and processing in real-world applications!
