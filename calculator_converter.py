def arithmetic():
    print("\n--- Basic Arithmetic ---")

    # Input validation for numbers
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input! Please enter numbers only.")

    # Input validation for operator
    while True:
        operator = input("Enter operator (+, -, *, /): ")

        if operator == "+":
            result = num1 + num2
            break

        elif operator == "-":
            result = num1 - num2
            break

        elif operator == "*":
            result = num1 * num2
            break

        elif operator == "/":
            if num2 == 0:
                print("Cannot divide by zero!")
            else:
                result = num1 / num2
                break

        else:
            print("Invalid operator! Please use +, -, * or /.")

    print("Result:", result)


def unit_converter():
    print("\n--- Unit Converter ---")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")

    # Validate menu choice
    while True:
        choice = input("Choose an option (1 or 2): ")

        if choice == "1" or choice == "2":
            break

        print("Invalid choice! Please enter 1 or 2.")

    # Validate value
    while True:
        try:
            value = float(input("Enter value: "))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    if choice == "1":
        miles = value * 0.621371
        print(f"{value} km = {miles:.2f} miles")

    elif choice == "2":
        fahrenheit = (value * 9 / 5) + 32
        print(f"{value}°C = {fahrenheit:.2f}°F")


def main():
    while True:
        print("\n==============================")
        print("   INTERACTIVE CALCULATOR")
        print("      UNIT CONVERTER")
        print("==============================")

        print("1. Basic Arithmetic")
        print("2. Unit Converter")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            arithmetic()

        elif choice == "2":
            unit_converter()

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


main()