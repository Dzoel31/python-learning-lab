# Simple Calculator Tests

import pytest

from learning.simple_calculator import add, subtract, multiply, divide, calculator

@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 3),
    (2.5, 3.5, 6.0),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300),
])
def test_add(x, y, expected):
    """Test the add function."""
    assert add(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (1, 2, -1),
    (2.5, 3.5, -1.0),
    (-1, 1, -2),
    (0, 0, 0),
    (100, 200, -100),
])
def test_subtract(x, y, expected):
    """Test the subtract function."""
    assert subtract(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 2),
    (2.5, 3.5, 8.75),
    (-1, 1, -1),
    (0, 0, 0),
    (100, 200, 20000),
])
def test_multiply(x, y, expected):
    """Test the multiply function."""
    assert multiply(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 0.5),
    (2.5, 3.5, 0.7142857142857143),
    (-1, 1, -1),
    (100, 200, 0.5),
    (5, 0, "ZeroDivisionError"),
    (0, 1, 0.0),
])
def test_divide(x, y, expected):
    """Test the divide function."""
    if expected == "ZeroDivisionError":
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero."):
            divide(x, y)
    else:
        assert divide(x, y) == expected



@pytest.mark.parametrize("x, y, operation, expected", [
    (1, 2, 'add', 3),
    (2.5, 3.5, 'add', 6.0),
    (1, 2, 'subtract', -1),
    (2.5, 3.5, 'subtract', -1.0),
    (1, 2, 'multiply', 2),
    (2.5, 3.5, 'multiply', 8.75),
    (1, 2, 'divide', 0.5),
    (2.5, 3.5, 'divide', 0.7142857142857143),
    (5, 0, 'divide', "ZeroDivisionError"),
    (0, 1, 'divide', 0.0),
    (1, 2, 'invalid', "ValueError"),
])
def test_calculator(x, y, operation, expected):
    """Test the calculator function."""
    if expected == "ZeroDivisionError":
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero."):
            calculator(x, y, operation)
    elif expected == "ValueError":
        with pytest.raises(ValueError, match="Invalid operation. Use 'add', 'subtract', 'multiply', or 'divide'."):
            calculator(x, y, operation)
    else:
        assert calculator(x, y, operation) == expected