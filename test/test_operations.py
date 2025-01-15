# tests/test_operations.py
import pytest
from src.operations import add, subtract, multiply, divide

# Test add function
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

# Test subtract function
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2

# Test multiply function
def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5

# Test divide function
def test_divide():
    assert divide(6, 2) == 3
    with pytest.raises(ValueError):  # Expecting an exception for division by zero
        divide(5, 0)
