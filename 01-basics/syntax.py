"""
Python Syntax Basics

Explanation:
- Python uses indentation (whitespace) to define code blocks,
  instead of curly braces {} like JavaScript.
- Each statement is usually written on its own line.
- No semicolons needed at the end of lines (unlike JS).
"""

# Example: indentation defines a block
if True:
    print("This is inside the if block")  # Output: This is inside the if block
print("This is outside the if block")     # Output: This is outside the if block

"""
Case sensitivity

Explanation:
Python is case-sensitive. "Age" and "age" are treated as different names.
"""

age = 25
Age = 30
print(age, Age)  # Output: 25 30