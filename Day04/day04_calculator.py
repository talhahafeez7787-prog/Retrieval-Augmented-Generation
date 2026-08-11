def calculator(num1, num2, operator):
    """
    Performs a calculation on two numbers based on the given operator.
    Returns the result, or an error message if invalid.
    """
    if operator == '+':                    # Addition
        return num1 + num2
    elif operator == '-':                  # Subtraction
        return num1 - num2
    elif operator == '*':                  # Multiplication
        return num1 * num2
    elif operator == '/':                  # Division
        if num2 == 0:                      # Prevent division by zero
            return "Error: Division by zero"
        return num1 / num2
    elif operator == '//':                 # Floor division (rounds down to nearest int)
        if num2 == 0:
            return "Error: Division by zero"
        return num1 // num2
    elif operator == '%':                  # Modulus (remainder after division)
        if num2 == 0:
            return "Error: Division by zero"
        return num1 % num2
    elif operator == '**':                 # Exponentiation (num1 raised to the power num2)
        return num1 ** num2
    else:
        return "Error: Invalid operator"   # Handle unsupported operator input


# ----- Main Program -----

# Get the first number from the user, convert input string to float
num1 = float(input("Enter first number: "))

# Show the user which operators are supported
print("Available operators: + - * / // % **")

# Get the operator as a string
operator = input("Enter operator: ")

# Get the second number from the user
num2 = float(input("Enter second number: "))

# Call the calculator function with the given inputs
result = calculator(num1, num2, operator)

# Display the final result
print(f"Result: {result}")