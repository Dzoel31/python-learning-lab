# Simple Calculator


def add(x: int | float, y: int | float) -> int | float:
    """
    Return the sum of x and y.

    Args:
        x (int | float): The first addend.
        y (int | float): The second addend.
    Returns:
        int | float: The result of the addition.
    """
    return x + y


def subtract(x: int | float, y: int | float) -> int | float:
    """
    Return the difference of x and y.

    Args:
        x (int | float): The minuend.
        y (int | float): The subtrahend.
    Returns:
        int | float: The result of the subtraction.
    """
    return x - y


def multiply(x: int | float, y: int | float) -> int | float:
    """
    Return the product of x and y.

    Args:
        x (int | float): The first multiplicand.
        y (int | float): The second multiplicand.

    Returns:
        int | float: The result of the multiplication.
    """
    return x * y


def divide(x: int | float, y: int | float) -> int | float:
    """
    Return the quotient of x and y.

    Args:
        x (int | float): The numerator.
        y (int | float): The denominator.
    Returns:
        int | float: The result of the division.
    Raises:
        ZeroDivisionError: If y is zero.
    """
    try:
        return x / y
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero.")


def calculator(x: int | float, y: int | float, operation: str) -> int | float:
    """
    Performs a basic arithmetic operation on two numbers.

    Args:
        x (int | float): The first operand.
        y (int | float): The second operand.
        operation (str): The operation to perform.
                        Must be one of 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
        int | float: The result of the arithmetic operation.

    Raises:
        ValueError: If the operation is not one of the supported types.
    """
    if operation == "add":
        return add(x, y)
    elif operation == "subtract":
        return subtract(x, y)
    elif operation == "multiply":
        return multiply(x, y)
    elif operation == "divide":
        return divide(x, y)
    else:
        raise ValueError(
            "Invalid operation. Use 'add', 'subtract', 'multiply', or 'divide'."
        )
