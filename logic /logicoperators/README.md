# Logic Operators

This exercise demonstrates boolean logic operators (AND, OR, NOT) for combining multiple conditions in decision-making processes.

## 📚 What You'll Learn

- AND operator for requiring all conditions to be true
- OR operator for requiring at least one condition to be true
- NOT operator for reversing boolean values
- Combining multiple logical operators
- Real-world applications of logical operations

## 🎯 Code Examples

### AND Operator Example (`and.py`)
```python
temp = 75
is_sunny = True

if temp < 0:
    print("It is below freezing who cares about the sun")
elif 0 < temp <= 32:
    if is_sunny:
        print("It is freezing and sunny")
    else:
        print("It is freezing and not sunny")
elif 32 < temp <= 60:
    if is_sunny:
        print("It is cool and sunny outside")
    else:
        print("It is cool and not sunny")
elif 60 < temp <= 80:
    if is_sunny:
        print("It is warm and sunny outside")
    else:
        print("It is warm and not sunny")
elif 80 < temp <= 100:
    if is_sunny:
        print("It is hot and sunny")
    else:
        print("It is hot and not sunny outside")
else:
    print("Immediate death its so hot out")
```

### OR Operator Example (`or.py`)
```python
temp = 31
is_raining = False

if temp > 85 or temp < 32 or is_raining:
    print("The event is canceled")
else:
    print("The event is still on")
```

## 🔧 Boolean Logic Operators

### AND Operator
Returns `True` only when **all** conditions are true.

```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")  # Both conditions must be true
```

**Truth Table for AND:**
| A | B | A and B |
|---|---|---------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

### OR Operator
Returns `True` when **at least one** condition is true.

```python
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("No work today")  # At least one condition must be true
```

**Truth Table for OR:**
| A | B | A or B |
|---|---|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

### NOT Operator
Reverses the boolean value.

```python
is_raining = False

if not is_raining:
    print("Good weather for a walk")  # True becomes False, False becomes True
```

**Truth Table for NOT:**
| A | not A |
|---|-------|
| True | False |
| False | True |

## 🚀 How to Run

1. Navigate to this folder:
   ```bash
   cd "logic /logicoperators"
   ```

2. Run either Python file:
   ```bash
   python3 and.py
   python3 or.py
   ```

3. **Expected Output**:
   - `and.py`: `"It is warm and sunny outside"`
   - `or.py`: `"The event is still on"`

## 💡 Try It Yourself

1. **Simple AND combinations**:
   ```python
   # Bank account access
   correct_pin = True
   sufficient_balance = True
   
   if correct_pin and sufficient_balance:
       print("Transaction approved")
   else:
       print("Transaction denied")
   
   # Age verification
   age = 20
   has_id = True
   
   if age >= 18 and has_id:
       print("Entry allowed")
   else:
       print("Entry denied")
   ```

2. **Simple OR combinations**:
   ```python
   # Emergency contact
   is_emergency = False
   is_doctor = True
   
   if is_emergency or is_doctor:
       print("Call allowed")
   else:
       print("Call blocked")
   
   # Payment methods
   has_cash = False
   has_card = True
   has_digital_wallet = False
   
   if has_cash or has_card or has_digital_wallet:
       print("Can make payment")
   else:
       print("Cannot make payment")
   ```

3. **Complex combinations**:
   ```python
   # User permissions
   is_admin = False
   is_moderator = True
   is_owner = False
   
   if is_admin or is_moderator or is_owner:
       print("Can delete posts")
   else:
       print("Cannot delete posts")
   
   # Login system
   username = "admin"
   password = "secret"
   is_active = True
   
   if (username == "admin" and password == "secret") and is_active:
       print("Login successful")
   else:
       print("Login failed")
   ```

## 🔍 Advanced Logic Operations

### Combining Multiple Operators
```python
# Complex weather system
temp = 75
humidity = 60
is_sunny = True
wind_speed = 10

# Perfect weather conditions
if (temp >= 70 and temp <= 80) and humidity < 70 and is_sunny and wind_speed < 15:
    print("Perfect weather!")
elif temp > 90 or humidity > 80 or wind_speed > 25:
    print("Extreme weather warning!")
else:
    print("Regular weather")
```

### Using Parentheses for Clarity
```python
# Without parentheses (might be confusing)
if age >= 18 and has_license or is_emergency:
    print("Can drive")

# With parentheses (clearer intention)
if (age >= 18 and has_license) or is_emergency:
    print("Can drive")
```

### Short-Circuit Evaluation
```python
# AND: If first condition is False, second is not evaluated
if False and print("This won't print"):
    pass

# OR: If first condition is True, second is not evaluated
if True or print("This won't print"):
    pass
```

## 🎯 Real-World Applications

### User Authentication
```python
def authenticate_user(username, password, is_active, account_locked):
    if username == "admin" and password == "secret123" and is_active and not account_locked:
        return "Login successful"
    else:
        return "Login failed"
```

### E-commerce Cart
```python
def can_checkout(has_items, payment_method, shipping_address, terms_accepted):
    if has_items and payment_method and shipping_address and terms_accepted:
        return "Checkout allowed"
    else:
        return "Complete all required fields"
```

### System Access Control
```python
def check_access(user_role, time_of_day, is_workday):
    # Admins can access anytime
    if user_role == "admin":
        return "Access granted"
    
    # Regular users only during work hours on workdays
    if user_role == "user" and (9 <= time_of_day <= 17) and is_workday:
        return "Access granted"
    
    return "Access denied"
```

### Grade Calculation
```python
def calculate_grade(homework_score, midterm_score, final_score, attendance):
    # Must pass all components
    if homework_score >= 60 and midterm_score >= 60 and final_score >= 60 and attendance >= 75:
        average = (homework_score + midterm_score + final_score) / 3
        return "Pass" if average >= 70 else "Conditional Pass"
    else:
        return "Fail"
```

## ⚠️ Common Mistakes

### 1. Using = Instead of ==
```python
# Wrong
if username = "admin" and password = "secret":
    print("Login successful")

# Correct
if username == "admin" and password == "secret":
    print("Login successful")
```

### 2. Forgetting Operator Precedence
```python
# This might not work as expected
if age >= 18 and has_license or is_emergency

# Clearer with parentheses
if (age >= 18 and has_license) or is_emergency
```

### 3. Redundant Boolean Comparisons
```python
# Redundant
if is_logged_in == True:
    print("Welcome")

# Better
if is_logged_in:
    print("Welcome")

# For False checks
if not is_logged_in:
    print("Please log in")
```

## 🔍 Operator Precedence

Order of evaluation (highest to lowest):
1. Parentheses `()`
2. NOT `not`
3. AND `and`
4. OR `or`

```python
# This expression:
if not a and b or c

# Is evaluated as:
if ((not a) and b) or c
```

## 🎯 Best Practices

1. **Use parentheses for clarity**:
   ```python
   # Good
   if (age >= 18 and has_license) or is_emergency:
   ```

2. **Keep conditions readable**:
   ```python
   # Good
   is_valid_user = username == "admin" and password == "secret"
   if is_valid_user and is_active:
   ```

3. **Use meaningful variable names**:
   ```python
   # Good
   has_permission = is_admin or is_moderator
   if has_permission:
   ```

## 🔗 Next Steps

After mastering logic operators, explore:
- [Conditionals](../conditionals/) - Ternary operators for concise logic
- [Loops](../../loops/) - Use logical conditions in iteration
- [Functions](../../functions/) - Create reusable logical operations

Boolean logic is essential for building complex decision-making systems in your programs!
