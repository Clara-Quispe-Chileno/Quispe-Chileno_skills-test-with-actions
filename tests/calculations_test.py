# System Modules
import sys
import os

# Installed Modules
import pytest

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci  # noqa: E402


def test_area_of_circle_positive_radius():
    """Test with a positive radius."""
    radius = 1
    result = area_of_circle(radius)
    assert abs(result - 3.14159) < 1e-5


def test_area_of_circle_zero_radius():
    """Test with radius = 0."""
    radius = 0
    result = area_of_circle(radius)
    assert result == 0


def test_area_of_circle_small_radius():
    """Test with a small decimal radius."""
    radius = 0.5
    result = area_of_circle(radius)
    assert result > 0


def test_area_of_circle_large_radius():
    """Test with a large radius."""
    radius = 100
    result = area_of_circle(radius)
    assert result > 0


def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    n = 0
    result = get_nth_fibonacci(n)
    assert result == 0


def test_get_nth_fibonacci_one():
    """Test with n=1."""
    n = 1
    result = get_nth_fibonacci(n)
    assert result == 1


def test_get_nth_fibonacci_two():
    """Test with n=2."""
    n = 2
    result = get_nth_fibonacci(n)
    assert result == 1


def test_get_nth_fibonacci_five():
    """Test with n=5."""
    n = 5
    result = get_nth_fibonacci(n)
    assert result == 5


def test_get_nth_fibonacci_ten():
    """Test with n=10."""
    n = 10
    result = get_nth_fibonacci(n)
    assert result == 55


def test_get_nth_fibonacci_large_value():
    """Test with a larger Fibonacci index."""
    n = 15
    result = get_nth_fibonacci(n)
    assert result == 610