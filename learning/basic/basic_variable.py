# Basic Variables

# This module covers the basic variable types in Python.

"""
Variables is like a vessel or container that holds data. Example:

```python
age = 30 # 'age' is a variable that holds the value 30
```

Python has several styles of naming variables, such as:

- Snake case: `my_variable_name`
- Camel case: `myVariableName`
- Leading underscore: `_my_variable`

But it cant start with a number or special character, and it is case-sensitive.

## Basic Variable Types

Python supports various types of variables, including integers, floats, strings,
and booleans.

- Integer: Whole numbers, both positive and negative. E.g., 10, -5, 0
- Float: Decimal numbers. E.g., 3.14, -0.001
- String: Sequence of characters enclosed in quotes. E.g., "Hello", 'World'
- Boolean: Represents True or False values.

Example of basic variable types:

```python
age = 30  # Integer
height = 172  # Integer (in centimeters)
weight = 50.5  # Float (in kilograms)
name = "John"  # String
is_student = True  # Boolean
```

You can use built-in functions like `type()` to check the type of a variable:
```python
print(type(age))  # Output: <class 'int'>
print(type(height))  # Output: <class 'int'>
print(type(weight))  # Output: <class 'float'>
print(type(name))  # Output: <class 'str'>
print(type(is_student))  # Output: <class 'bool'>
```

## Example of using these variables

```python
print(f"{name} is {age} years old, {height} cm tall, weighs {weight} kg, and it is "
      f"{is_student} that he is a student.")
```
it will output:
```John is 30 years old, 172 cm tall, weighs 50.5 kg, and it is True that \
    he is a student.
```
"""


def basic_variable_types():
    # Integer
    age = 30
    print("Age:", age)
    print("Type of age:", type(age))

    # Integer
    height = 172  # in centimeters
    print("Height:", height)
    print("Type of height:", type(height))

    # Float
    weight = 50.5  # in kilograms
    print("Weight:", weight)
    print("Type of weight:", type(weight))

    # String
    name = "John"
    print("Name:", name)
    print("Type of name:", type(name))

    # Boolean
    is_student = True
    print("Is Student:", is_student)
    print("Type of is_student:", type(is_student))

    # Example of using these variables
    print(
        f"{name} is {age} years old, {height} cm tall, weighs {weight} kg, and it is "
        f"{is_student} that he is a student."
    )

    return {
        "age": age,
        "height": height,
        "weight": weight,
        "name": name,
        "is_student": is_student,
    }
