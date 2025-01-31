import pytest
from calculator import calculator

# Test cases for add, subtract, multiply, divide
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, -1, -2),
    (0, 5, 5),
    (3.5, 2.5, 6.0),
])
def test_add(a, b, expected):
    """Test addition function with multiple cases."""
    assert calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 2, 3),
    (-1, -1, 0),
    (0, 5, -5),
    (3.5, 2.5, 1.0),
])
def test_subtract(a, b, expected):
    """Test subtraction function with multiple cases."""
    assert calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-1, -1, 1),
    (0, 5, 0),
    (3.5, 2.5, 8.75),
])
def test_multiply(a, b, expected):
    """Test multiplication function with multiple cases."""
    assert calculator.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (-10, -2, 5),
    (7, 2, 3.5),
])
def test_divide(a, b, expected):
    """Test division function with valid cases."""
    assert calculator.divide(a, b) == expected

def test_divide_by_zero():
    """Test that dividing by zero raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(10, 0)
