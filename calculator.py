# calculator.py
"""
A simple calculator utility that supports basic arithmetic operations.
Supports addition, subtraction, multiplication, division,
power, modulus, and square root operations.
Handles invalid inputs and division by zero gracefully.
"""

import math


def add(x, y):
    """Return the sum of x and y."""
    return x + y


def subtract(x, y):
    """Return the difference of x and y."""
    return x - y


def multiply(x, y):
    """Return the product of x and y."""
    return x * y


def divide(x, y):
    """Return the division of x by y. Raise ValueError on division by zero."""
    if y == 0:
        raise ValueError("Division by zero is not allowed.")
    return x / y


def power(x, y):
    """Return x raised to the power y."""
    return x ** y


def modulus(x, y):
    """Return the modulus of x by y."""
    if y == 0:
        raise ValueError("Modulus by zero is not allowed.")
    return x % y


def square_root(x):
    """Return the square root of x. Raise ValueError if x is negative."""
    if x < 0:
        raise ValueError("Square root of negative number is not defined in real numbers.")
    return math.sqrt(x)


def get_number(prompt):
    """Prompt the user for a number until a valid float is entered."""
    while True:
        val = input(prompt)
        try:
            number = float(val)
            return number
        except ValueError:
            print(f"Invalid input '{val}'. Please enter a numeric value.")


def get_operation():
    """Prompt the user to select a valid operation."""
    operations = {
        '+': 'addition',
        '-': 'subtraction',
        '*': 'multiplication',
        '/': 'division',
        '^': 'power',
        '%': 'modulus',
        'sqrt': 'square root'
    }
    print("Choose operation:")
    for op, name in operations.items():
        print(f"  {op} : {name}")
    while True:
        op = input("Enter operation symbol: ").strip().lower()
        if op in operations:
            return op
        else:
            print(f"Invalid operation '{op}'. Please select a valid operation.")


def main():
    """Main function to run the calculator script."""
    print("Welcome to the simple calculator!")

    operation = get_operation()

    try:
        if operation == 'sqrt':
            # Only one operand needed
            num1 = get_number("Enter the number to find square root of: ")
            result = square_root(num1)
            print(f"sqrt({num1}) = {result}")
        else:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            elif operation == '^':
                result = power(num1, num2)
            elif operation == '%':
                result = modulus(num1, num2)
            else:
                print("Unsupported operation.")
                return

            print(f"{num1} {operation} {num2} = {result}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
