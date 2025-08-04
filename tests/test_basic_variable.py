# Test for basic_variable_types function

import pytest

from learning.basic.basic_variable import basic_variable_types

def test_basic_variable_types():
    result = basic_variable_types()
    assert result["age"] == 30
    assert result["height"] == 172
    assert result["weight"] == 50.5
    assert result["name"] == "John"
    assert result["is_student"] is True

@pytest.mark.parametrize(
    "var_type, expected",
    [
        ("age", 30),
        ("height", 172),
        ("weight", 50.5),
        ("name", "John"),
        ("is_student", True),
    ]
)
def test_basic_variable_types_parametrized(var_type, expected):
    result = basic_variable_types()
    assert result[var_type] == expected

@pytest.mark.parametrize(
    "var_type, expected_type",
    [
        ("age", int),
        ("height", int),
        ("weight", float),
        ("name", str),
        ("is_student", bool),
    ]
)
def test_basic_variable_types_type(var_type, expected_type):
    result = basic_variable_types()
    assert isinstance(result[var_type], expected_type)
