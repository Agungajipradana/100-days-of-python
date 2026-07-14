"""
Displaying Output with print()

Explanation:
print() is the most common way to display information
to the console in Python.
"""

print("Hello, World!")  # Output: Hello, World!

"""
1. Printing Multiple Values

Explanation:
You can print multiple values separated by commas.
Python automatically adds a space between them.
"""

print("Name:", "John", "Age:", 25)
# Output: Name: John Age: 25

"""
2. String Formatting with f-strings

Explanation:
f-strings (formatted string literals) let you embed variables
directly inside a string using curly braces {}.
This is similar to template literals in JavaScript.
"""

name = "John"
print(f"Hello, {name}!")  # Output: Hello, John!

"""
3. Custom Separator and Line Ending
"""

print("Python", "is", "fun", sep="-")   # Output: Python-is-fun
print("No new line here", end=" ")      # Output: No new line here (no line break after)
print("continued on the same line")     # Output: continued on the same line