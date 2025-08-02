# My Calculator 

print("🧮 Welcome to the Yvonne Calculator!")

while True:
    try:
#first number
        num1 = float(input("\nEnter the first number: "))

        # Choose the sign to use
        operation = input("Choose an operation (+, -, *, x, /, ÷): ").strip()

        # second number
        num2 = float(input("Enter the second number: "))

        # operation
        if operation == "+":
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif operation == "-":
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif operation in ["*", "x", "X"]:
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif operation in ["/", "÷"]:
            if num2 != 0:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
            else:
                print("⚠️ Error: Division by zero is not allowed.")
        else:
            print("❌ Invalid operation. Please choose from +, -, *, x, /, ÷")

    except ValueError:
        print("⚠️ Error: Please enter valid numbers.")

    # Testing testing
    again = input("\nWould you like to calculate again? (yes/no): ").strip().lower()
    if again != "yes":
        print("👋 Thanks for using my calculator. Goodbye!")
        break
