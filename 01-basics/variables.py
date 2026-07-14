"""
How to Create a Variable

In Python, you don't need to declare a type before a variable name.
Just assign a value directly using the "=" operator, and Python
will automatically detect the data type.
"""

name = "John"       # This creates a string variable
age = 25            # This creates an integer variable

"""
1. Basic Variable Creation

Explanation:
A variable is created the moment you assign a value to it.
No need for "let", "const", or "var" like in JavaScript.
"""

city = "Jakarta"
print(city)  # Output: Jakarta

"""
2. Checking the Data Type

Explanation:
Python has a built-in function called type() that tells you
what kind of data is stored in a variable.
"""

score = 90
print(type(score))  # Output: <class 'int'>

"""
3. Dynamic Typing

Explanation:
Python is dynamically typed, meaning a variable's type can
change if you assign a different type of value to it later.
"""

data = 10
print(type(data))  # Output: <class 'int'>

data = "now I'm a string"
print(type(data))  # Output: <class 'str'>

"""
4. Multiple Assignment
"""

x, y, z = 1, 2, 3
print(x, y, z)  # Output: 1 2 3

"""
5. Naming Rules

Explanation:
- Can contain letters, numbers, and underscores
- Cannot start with a number
- Case-sensitive
- Convention: use snake_case (e.g. first_name)
"""

first_name = "Ahmad"
print(first_name)  # Output: Ahmad