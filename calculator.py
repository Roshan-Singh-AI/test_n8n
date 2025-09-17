# calculator.py
"""
Simple calculator module to perform basic arithmetic operations.
Supports addition, subtraction, multiplication, division,
power, modulus, and square root operations.
"""

import math


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the division of a by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


def power(a, b):
    """Return a raised to the power of b."""
    return a ** b


def modulus(a, b):
    """Return the modulus of a by b."""
    return a % b


def square_root(a):
    """Return the square root of a.

    Raises:
        ValueError: If a is negative.
    """
    if a < 0:
        raise ValueError("Square root of negative number is not allowed.")
    return math.sqrt(a)
