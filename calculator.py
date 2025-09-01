def get_operation():
    operation = input("Choose operation (+, -, *, /): ")
    if operation in ["+", "-", "*", "/"]:
        return operation
    else:
        return None
def get_number(prompt):
    user_input = input(prompt)
    try:
        number = float(user_input)
        return number
    except ValueError:
        return None
def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
def main():
    print("=== Simple Calculator ===")

    while True:
        # 1) get operation
        operation = get_operation()
        if operation is None:
            print("Invalid operation. Please choose one of +, -, *, /.\n")
            continue

        # 2) get first number
        num1 = get_number("Enter first number: ")
        if num1 is None:
            print("Invalid number. Please try again.\n")
            continue

        # 3) get second number
        num2 = get_number("Enter second number: ")
        if num2 is None:
            print("Invalid number. Please try again.\n")
            continue

        # 4) division by zero check
        if operation == "/" and num2 == 0:
            print("Error: Division by zero is not allowed.\n")
            continue

        # 5) calculate
        result = calculate(num1, num2, operation)

        # 6) show result
        print(f"Result: {num1} {operation} {num2} = {result}\n")

        # 7) ask to continue
        again = input("Do you want to calculate again? (y/n): ").strip().lower()
        if again == "n":
            print("Goodbye!")
            break
        print()  # blank line for readability

if __name__ == "__main__":
    main()
