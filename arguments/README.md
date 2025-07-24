# Function Arguments

This section covers different types of function arguments in Python, including default arguments, keyword arguments, and arbitrary arguments (*args and **kwargs).

## 📋 Files in this Section

### 1. Default Arguments (`defaultargs.py`)
Learn how to create functions with default parameter values.

**Key Concepts:**
- Setting default values for function parameters
- Optional parameters in function calls
- Parameter order with default values

**Examples:**
- `net_price()` - Calculate price with optional discount and tax
- `count()` - Countdown function with optional start parameter

**Run the file:**
```bash
python3 defaultargs.py
```

### 2. Keyword Arguments (`keywordarguments.py`)
Understand how to use keyword arguments for more readable function calls.

**Key Concepts:**
- Named arguments in function calls
- Order independence with keyword arguments
- Built-in keyword arguments (like `end` in print)

**Examples:**
- `hello()` - Greeting function with multiple named parameters
- Using `end` parameter with print function

**Run the file:**
```bash
python3 keywordarguments.py
```

### 3. Arbitrary Arguments (`arbitraryarguments.py`)
Master the use of *args and **kwargs for flexible function parameters.

**Key Concepts:**
- `*args` - Variable number of positional arguments
- `**kwargs` - Variable number of keyword arguments
- Combining both in a single function

**Examples:**
- `add()` - Sum function accepting any number of arguments
- `display_name()` - Print function for multiple name parts
- `print_address()` - Address printer using **kwargs
- `shipping_label()` - Complete shipping label using both *args and **kwargs

**Run the file:**
```bash
python3 arbitraryarguments.py
```

## 🎯 Learning Objectives

After completing this section, you should understand:

1. **Default Arguments**: How to make function parameters optional with default values
2. **Keyword Arguments**: How to call functions using parameter names for clarity
3. **Arbitrary Arguments**: How to create flexible functions that accept varying numbers of arguments
4. **Best Practices**: When and how to use each type of argument effectively

## 🚀 Quick Start

1. Navigate to the arguments folder:
   ```bash
   cd arguments
   ```

2. Run any of the example files:
   ```bash
   python3 defaultargs.py
   python3 keywordarguments.py
   python3 arbitraryarguments.py
   ```

## 📚 Recommended Learning Order

1. **Default Arguments** - Start with optional parameters
2. **Keyword Arguments** - Learn named parameter calling
3. **Arbitrary Arguments** - Master flexible function design

## 🔗 Related Topics

- [Basic Functions](../basic-functions/) - Foundation of function concepts
- [Logic](../logic%20/) - Using arguments in conditional logic

---

**Next Steps**: After mastering function arguments, consider exploring more advanced topics like decorators, lambda functions, and object-oriented programming.
