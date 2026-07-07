def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the division of two numbers. Handles division by zero."""
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


def calculator():
    """Run the calculator until the user chooses to exit."""
    while True:
        print("\n--- Simple Calculator ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "5":
            print("Calculator closed.")
            break

        if choice in ["1", "2", "3", "4"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print("Result =", add(num1, num2))
            elif choice == "2":
                print("Result =", subtract(num1, num2))
            elif choice == "3":
                print("Result =", multiply(num1, num2))
            elif choice == "4":
                print("Result =", divide(num1, num2))
        else:
            print("Invalid choice! Please try again.")


calculator()