# Loops

This section demonstrates different types of loops in Python for repetitive execution and iteration.

## 📚 What You'll Learn

- While loops for conditional repetition
- For loops for iterating over sequences
- Loop control and exit conditions
- Practical applications of loops
- Avoiding infinite loops

## 🔄 Loop Types

### While Loops
Execute code repeatedly as long as a condition is true.

### For Loops
Iterate over sequences like lists, strings, or ranges.

### Compound Interest
Apply loops to solve real-world mathematical problems.

## 📁 Files in This Section

### 1. While Loops (`whileloops.py`)
```python
# Name validation loop
name = input("Enter your name: ")
while(name == ""):
    print("You did not enter your name")
    name = input("Please enter your name: ")
print(f"Hello {name}")

# Food collection loop
food = input("Enter a food you like ('q' to quit) ")
while food.lower() != 'q':
    print(f"{food}")
    food = input("Enter another food you like ('q' to quit) ")
```

**Key Concepts:**
- Input validation with while loops
- Loop exit conditions
- String methods in loop conditions
- Collecting user input until a sentinel value

### 2. For Loops (`forloops.py`)
**Purpose:** Basic for loop demonstrations

**What it covers:**
- Simple for loop iteration
- Range function usage
- Basic loop structure

### 3. Compound Interest (`compoundinterest.py`)
**Purpose:** Financial calculations using loops

**What it covers:**
- Compound interest formula implementation
- Mathematical calculations in loops
- Real-world application of iteration
- Financial modeling concepts

### 4. Countdown Timer (`countdown.py`) ⭐ NEW
**Purpose:** Interactive countdown timer with time formatting

**What it covers:**
- Time manipulation and formatting (HH:MM:SS)
- Real-time countdown using `time.sleep()`
- Mathematical time calculations (hours, minutes, seconds)
- User input for countdown duration
- Practical loop applications

**Key Features:**
- Professional time display format
- Real-time updates
- User-defined countdown duration
- Mathematical time conversion

### 5. Nested Loops (`nestedforloop.py`) ⭐ NEW
**Purpose:** Pattern generation using nested loop structures

**What it covers:**
- Nested loop concepts
- User input for dimensions and symbols
- Pattern creation and visual output
- Dynamic formatting
- Two-dimensional iteration

**Key Features:**
- Custom pattern dimensions
- User-defined symbols
- Visual programming concepts
- Grid-based output

## 🎯 While Loop Examples

### Basic Structure
```python
while condition:
    # Code to execute
    # Update condition variable
```

### Input Validation
```python
age = int(input("Enter your age: "))
while age <= 0:
    print("Age must be positive!")
    age = int(input("Enter your age: "))
```

### Counting Loop
```python
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1
```

## 🚀 How to Run

1. Navigate to this folder:
   ```bash
   cd loops
   ```

2. Run any Python file:
   ```bash
   python3 whileloops.py
   ```

3. **Follow the prompts** for interactive examples

## 💡 Try It Yourself

1. **Test the while loop examples**:
   - Try entering an empty name to see validation
   - Enter different foods and 'q' to quit

2. **Create your own while loops**:
   ```python
   # Password checker
   password = input("Enter password: ")
   while password != "secret123":
       print("Incorrect password!")
       password = input("Enter password: ")
   print("Access granted!")
   
   # Number guessing game
   import random
   secret = random.randint(1, 10)
   guess = 0
   while guess != secret:
       guess = int(input("Guess a number (1-10): "))
       if guess < secret:
           print("Too low!")
       elif guess > secret:
           print("Too high!")
   print("You got it!")
   ```

3. **Practice with for loops** (when you add content to forloops.py):
   ```python
   # Count from 1 to 10
   for i in range(1, 11):
       print(i)
   
   # Iterate over a string
   word = "Python"
   for letter in word:
       print(letter)
   
   # Iterate over a list
   fruits = ["apple", "banana", "orange"]
   for fruit in fruits:
       print(f"I like {fruit}")
   ```

## ⚠️ Common Mistakes

### 1. Infinite Loops
```python
# Wrong - this will run forever
count = 1
while count <= 10:
    print(count)
    # Missing: count += 1

# Correct
count = 1
while count <= 10:
    print(count)
    count += 1  # Don't forget to update the condition variable!
```

### 2. Off-by-One Errors
```python
# Be careful with range boundaries
for i in range(10):  # This goes from 0 to 9, not 1 to 10
    print(i)

# If you want 1 to 10:
for i in range(1, 11):
    print(i)
```

### 3. Modifying Loop Variables
```python
# Be careful when modifying the loop variable inside the loop
for i in range(5):
    print(i)
    i = 10  # This doesn't affect the loop!
```

## 🔍 Key Concepts

1. **Loop Conditions**: Boolean expressions that control loop execution
2. **Loop Variables**: Variables that change during each iteration
3. **Sentinel Values**: Special values that signal loop termination
4. **Input Validation**: Using loops to ensure valid user input
5. **Infinite Loops**: Loops that never terminate (usually bugs)

## 🎯 Real-World Applications

- **User Input Validation**: Ensure users enter valid data
- **Menu Systems**: Display options until user chooses to exit
- **Data Processing**: Process items in a list or file
- **Game Logic**: Main game loops that run until game over
- **Calculations**: Compound interest, iterative algorithms

## 🔗 Next Steps

After mastering loops, consider:
- [Format Specifiers](../format-specifiers/) - Better output formatting
- [Functions](../functions/) - Reusable code blocks (when added)
- [Lists](../lists/) - Data structures to iterate over (when added)
- [File I/O](../file-io/) - Reading and processing files (when added)

Loops are fundamental to programming - they're used in almost every significant program!
