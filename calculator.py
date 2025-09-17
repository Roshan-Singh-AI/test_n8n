import math


def get_number(prompt):
    """Prompt the user to enter a number and validate the input."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_operation():
    """Prompt the user to select an operation and validate the choice."""
    operations = ['+', '-', '*', '/', '**', '%', 'sqrt']
    print("Select an operation:")
    print("Addition (+)")
    print("Subtraction (-)")
    print("Multiplication (*)")
    print("Division (/)")
    print("Power (**)")
    print("Modulus (%)")
    print("Square root (sqrt)")

    while True:
        op = input("Enter operation: ").strip()
        if op in operations:
            return op
        else:
            print(f"Invalid operation. Please choose from {operations}.")


def calculate(num1, num2, operation):
    """Perform calculation based on the operation."""
    try:
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            if num2 == 0:
                return 'Error: Division by zero is undefined.'
            return num1 / num2
        elif operation == '**':
            return num1 ** num2
        elif operation == '%':
            if num2 == 0:
                return 'Error: Modulus by zero is undefined.'
            return num1 % num2
        elif operation == 'sqrt':
            if num1 < 0:
                return 'Error: Cannot take square root of negative number.'
            return math.sqrt(num1)
        else:
            return 'Error: Unsupported operation.'
    except Exception as e:
        return f'Error: {str(e)}'


def main():
    print("Simple Calculator")
    operation = get_operation()

    if operation == 'sqrt':
        num1 = get_number("Enter number to find square root of: ")
        result = calculate(num1, None, operation)
        if isinstance(result, float):
            print(f"sqrt({num1}) = {result}")
        else:
            print(result)
    else:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        result = calculate(num1, num2, operation)
        if isinstance(result, float):
            print(f"{num1} {operation} {num2} = {result}")
        else:
            print(result)


if __name__ == '__main__':
    main()
