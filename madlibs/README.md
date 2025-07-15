# Mad Libs

This exercise demonstrates how to create an interactive story game using string manipulation, user input, and f-string formatting.

## 📚 What You'll Learn

- String manipulation and formatting
- Creating interactive programs with multiple inputs
- Using f-strings for dynamic text generation
- Building engaging user experiences
- Combining multiple programming concepts

## 🎭 How It Works

Mad Libs is a word game where:
1. The program asks for different types of words (adjectives, nouns, verbs)
2. The user provides words without knowing the story context
3. The program inserts these words into a pre-written story template
4. The result is usually a funny or unexpected story

## 🎯 Code Breakdown

```python
adjective1 = input("Input the first adjective: ")
noun1 = input("Input noun1: ")
adjective2 = input("Input the second adjective: ")
verb1 = input("Enter a verb: ")
adjective3 = input("Enter the third adjective: ")

print(f"Today i want to a {adjective1} zoo")
print(f"In an exhibit i saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}")
```

## 📖 Story Template

The current story is about a zoo visit:
```
Today I want to go to a [adjective1] zoo
In an exhibit I saw a [noun1]
[noun1] was [adjective2] and [verb1]
I was [adjective3]
```

## 🚀 How to Run

1. Navigate to this folder:
   ```bash
   cd madlibs
   ```

2. Run the Python file:
   ```bash
   python3 madlibs.py
   ```

3. **Follow the prompts**:
   ```
   Input the first adjective: silly
   Input noun1: elephant
   Input the second adjective: purple
   Enter a verb: dancing
   Enter the third adjective: amazed
   ```

4. **Example Output**:
   ```
   Today i want to a silly zoo
   In an exhibit i saw a elephant
   elephant was purple and dancing
   I was amazed
   ```

## 💡 Try It Yourself

1. **Test different word types**:
   - Try funny adjectives: "slimy", "gigantic", "sparkly"
   - Try unusual nouns: "banana", "spaceship", "penguin"
   - Try action verbs: "exploding", "singing", "flying"

2. **Enhance the story**:
   ```python
   # Add more word types
   color = input("Enter a color: ")
   number = input("Enter a number: ")
   food = input("Enter a food: ")
   
   # Expand the story
   print(f"Today I want to go to a {adjective1} zoo")
   print(f"I brought {number} {color} {food} to eat")
   print(f"In an exhibit I saw a {noun1}")
   print(f"The {noun1} was {adjective2} and {verb1}")
   print(f"I was {adjective3} and decided to go home")
   ```

3. **Create new story templates**:
   ```python
   # Space adventure story
   print("🚀 SPACE ADVENTURE 🚀")
   spaceship = input("Name of a vehicle: ")
   planet = input("Name of a place: ")
   alien = input("Type of animal: ")
   action = input("Action verb: ")
   
   print(f"I flew my {spaceship} to {planet}")
   print(f"There I met a {alien} who was {action}")
   
   # Cooking story
   print("👨‍🍳 COOKING DISASTER 👨‍🍳")
   ingredient = input("Food ingredient: ")
   kitchen_tool = input("Kitchen tool: ")
   adjective = input("Adjective: ")
   
   print(f"I tried to cook {ingredient} with a {kitchen_tool}")
   print(f"The result was {adjective}!")
   ```

## ⚠️ Current Issues to Fix

### Grammar Issues
The current story has some grammar problems:
```python
# Current (incorrect):
print(f"Today i want to a {adjective1} zoo")

# Better:
print(f"Today I want to go to a {adjective1} zoo")
```

### Article Usage
```python
# Better handling of articles (a/an):
def get_article(word):
    if word[0].lower() in 'aeiou':
        return 'an'
    else:
        return 'a'

article = get_article(noun1)
print(f"In an exhibit I saw {article} {noun1}")
```

## 🔍 Key Concepts Demonstrated

1. **User Input**: Getting multiple inputs from the user
2. **String Formatting**: Using f-strings to embed variables
3. **Sequential Programming**: Following a logical flow
4. **Creative Programming**: Building something fun and interactive
5. **Variable Usage**: Storing and reusing user input

## 🎨 Enhancement Ideas

1. **Random Story Selection**: Choose from multiple story templates
2. **Input Validation**: Check if words match requested types
3. **Story Themes**: Categories like adventure, horror, comedy
4. **Save Stories**: Write completed stories to files
5. **Multiple Players**: Let multiple people contribute words

### Example Enhancement:
```python
import random

stories = [
    "The {adjective1} {noun1} {verb1} to the {adjective2} {noun2}",
    "Yesterday, a {adjective1} {noun1} was {verb1} in the {noun2}",
    "The {adjective2} {noun1} {verb1} when it saw the {adjective1} {noun2}"
]

# Get user input
adjective1 = input("First adjective: ")
noun1 = input("First noun: ")
# ... more inputs

# Select random story
selected_story = random.choice(stories)
print(selected_story.format(
    adjective1=adjective1, 
    noun1=noun1, 
    verb1=verb1, 
    adjective2=adjective2, 
    noun2=noun2
))
```

## 🔗 Next Steps

After mastering Mad Libs, you've completed the fundamentals! Consider exploring:
- **File I/O**: Reading stories from files
- **Functions**: Creating reusable code blocks
- **Lists**: Storing multiple story templates
- **Loops**: Creating continuous gameplay
- **Classes**: Building a complete game system

Mad Libs is a great capstone project that combines all the Python fundamentals you've learned!
