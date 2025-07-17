# String Indexing

This exercise demonstrates how to access individual characters and extract substrings from strings using indexing and slicing.

## 📚 What You'll Learn

- Accessing individual characters with indexing
- Extracting substrings with slicing
- Understanding positive and negative indices
- String reversal and step values
- Practical applications for data processing

## 🎯 Code Example

```python
credit_number = "1234-5678-9012-3456"

# Extract last four digits
last_four = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_four}")  # "XXXX-XXXX-XXXX-3456"

# Reverse the string
reverse_number = credit_number[::-1]
print(f"{reverse_number}")  # "6543-2109-8765-4321"
```

## 🔢 String Indexing Basics

### Positive Indexing
```python
text = "Python"
#      012345
print(text[0])    # 'P'
print(text[1])    # 'y'
print(text[5])    # 'n'
```

### Negative Indexing
```python
text = "Python"
#      -6-5-4-3-2-1
print(text[-1])   # 'n'
print(text[-2])   # 'o'
print(text[-6])   # 'P'
```

## ✂️ String Slicing

### Basic Slicing Syntax
```python
string[start:end:step]
```

### Slicing Examples
```python
credit_number = "1234-5678-9012-3456"

# First 4 characters
print(credit_number[:4])     # "1234"

# Characters 5-9
print(credit_number[5:9])    # "5678"

# From index 5 to end
print(credit_number[5:])     # "5678-9012-3456"

# Last 4 characters
print(credit_number[-4:])    # "3456"

# Every other character
print(credit_number[::2])    # "13-689-35"

# Reverse string
print(credit_number[::-1])   # "6543-2109-8765-4321"
```

## 🚀 How to Run

1. Navigate to this folder:
   ```bash
   cd "strings/string indexing"
   ```

2. Run the Python file:
   ```bash
   python3 string-indexing.py
   ```

3. **Expected Output**:
   ```
   XXXX-XXXX-XXXX-3456
   6543-2109-8765-4321
   ```

## 💡 Try It Yourself

1. **Practice with different strings**:
   ```python
   # Phone number formatting
   phone = "1234567890"
   formatted = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
   print(formatted)  # "(123) 456-7890"
   
   # Email extraction
   email = "user@example.com"
   username = email[:email.find('@')]
   domain = email[email.find('@')+1:]
   print(f"Username: {username}")  # "user"
   print(f"Domain: {domain}")      # "example.com"
   ```

2. **Text processing**:
   ```python
   # Extract initials
   name = "John Doe Smith"
   words = name.split()
   initials = ''.join([word[0] for word in words])
   print(initials)  # "JDS"
   
   # File extension
   filename = "document.pdf"
   extension = filename[filename.rfind('.')+1:]
   print(extension)  # "pdf"
   ```

3. **Data validation**:
   ```python
   # Check if string starts/ends with specific characters
   url = "https://www.example.com"
   if url[:8] == "https://":
       print("Secure URL")
   
   # Extract file name from path
   path = "/home/user/documents/file.txt"
   filename = path[path.rfind('/')+1:]
   print(filename)  # "file.txt"
   ```

## 🔍 Advanced Techniques

### Step Values
```python
text = "Programming"
print(text[::2])    # "Pormmn" (every 2nd character)
print(text[1::2])   # "rgain" (every 2nd, starting from index 1)
print(text[::-2])   # "gimrgr" (every 2nd in reverse)
```

### Boundary Handling
```python
text = "Python"
# Python handles out-of-bounds gracefully with slicing
print(text[10:20])  # "" (empty string, not error)
print(text[-10:])   # "Python" (starts from beginning)
```

### Common Patterns
```python
# Get first and last character
text = "Hello"
first_last = text[0] + text[-1]  # "Ho"

# Remove first and last character
middle = text[1:-1]  # "ell"

# Check if palindrome
word = "racecar"
is_palindrome = word == word[::-1]  # True
```

## ⚠️ Common Mistakes

### 1. Index Out of Range
```python
text = "Hi"
# print(text[5])  # IndexError: string index out of range

# Safe approach:
if len(text) > 5:
    print(text[5])
```

### 2. Forgetting Negative Indexing
```python
text = "Python"
# Wrong way to get last character
# last_char = text[len(text)]  # IndexError

# Correct ways
last_char = text[-1]
last_char = text[len(text)-1]
```

### 3. Slicing Confusion
```python
text = "Hello"
# Remember: [start:end] - end is exclusive
print(text[1:4])    # "ell" (not "ello")
print(text[1:])     # "ello" (from index 1 to end)
```

## 🎯 Real-World Applications

### Data Masking
```python
def mask_credit_card(card_number):
    return "XXXX-XXXX-XXXX-" + card_number[-4:]

def mask_ssn(ssn):
    return "XXX-XX-" + ssn[-4:]
```

### Text Processing
```python
def get_file_parts(filename):
    dot_index = filename.rfind('.')
    if dot_index != -1:
        name = filename[:dot_index]
        extension = filename[dot_index+1:]
        return name, extension
    return filename, ""
```

### Data Validation
```python
def validate_format(text, pattern):
    # Check if text matches expected pattern length/format
    if len(text) != len(pattern):
        return False
    
    for i, char in enumerate(pattern):
        if char == 'X' and not text[i].isdigit():
            return False
        elif char == 'A' and not text[i].isalpha():
            return False
    return True

# Usage: validate_format("ABC123", "AAAXXX")
```

## 🔗 Next Steps

After mastering string indexing, move on to:
- [String Methods](../string-methods/) - Learn built-in string functions
- [Format Specifiers](../../format-specifiers/) - Advanced string formatting
- [Loops](../../loops/) - Iterate through strings character by character

String indexing is foundational for text processing and data manipulation in Python!
