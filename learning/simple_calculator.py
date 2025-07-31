# Simple Calculator

def add(x: int | float, y: int | float) -> int | float:
    """Return the sum of x and y."""
    return x + y

def subtract(x: int | float, y: int | float) -> int | float:
    """Return the difference of x and y."""
    return x - y

def multiply(x: int | float, y: int | float) -> int | float:
    """Return the product of x and y."""
    return x * y

def divide(x: int | float, y: int | float) -> int | float:
    """Return the quotient of x and y, raising ZeroDivisionError if division by zero occurs."""
    try:
        return x / y
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero.")

def calculator(x: int | float, y: int | float, operation: str) -> int | float:
    """Perform a calculation based on the operation provided."""
    if operation == 'add':
        return add(x, y)
    elif operation == 'subtract':
        return subtract(x, y)
    elif operation == 'multiply':
        return multiply(x, y)
    elif operation == 'divide':
        return divide(x, y)
    else:
        raise ValueError("Invalid operation. Use 'add', 'subtract', 'multiply', or 'divide'.")