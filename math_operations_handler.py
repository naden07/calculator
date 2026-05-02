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

    return 0

def get_number_input(prompt):
    """Ensures the user provides a valid number, capturing input errors."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def main():
    print("--- SIMPLE MATH HANDLER ---")

    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("\nEnter choice (1/2/3/4): ").strip()

        if choice in ['1', '2', '3', '4']:
            try:
                n1 = get_number_input("Enter first number: ")
                n2 = get_number_input("Enter second number: ")

                result = perform_calculation(choice, n1, n2)
                print(f"\n>> The result is: {result}")

            except ZeroDivisionError as e:
                print(f"\n{e}")
            except Exception as e:
                print(f"\nAn unexpected error occurred: {e}")
        else:
            print("Invalid selection. Please choose a number from 1 to 4.")