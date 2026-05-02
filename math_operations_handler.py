import sys

def perform_calculation(operation, num1, num2):
    """Handles the math logic and returns the result."""
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        if num2 == 0:
            raise ZeroDivisionError("Error: Division by zero is not allowed.")
        return num1 / num2

def get_number_input(prompt):
    """Ensures the user provides a valid number, capturing input errors."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

