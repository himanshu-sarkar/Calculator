def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(a, b):
    return a ** b


history = []

print("=" * 35)
print("        SIMPLE CALCULATOR")
print("=" * 35)


while True:
    try:
        print("\nEnter your numbers:")
        a = float(input("First number: "))
        b = float(input("Second number: "))
    except ValueError:
        print("\nInvalid number entered. Please try again.")
        print("-" * 35)
        continue

    op = input("Operation (+ - * / **): ")

    print("\n" + "-" * 35)

    result = None

    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = subtract(a, b)
    elif op == "*":
        result = multiply(a, b)
    elif op == "/":
        result = divide(a, b)
    elif op == "**":
        result = power(a, b)
    else:
        print("Invalid operation")

    if result is not None:
        print("Result:", result)
        history.append(f"{a} {op} {b} = {result}")

    print("-" * 35)

    view = input("Do you want to see calculation history? (y/n): ")
    if view.lower() == "y":
        print("\n--- Calculation History ---")
        for item in history:
            print(item)
        print("----------------------------")

    again = input("Do you want to continue? (y/n): ")
    if again.lower() != "y":
        print("\nThank you for using the calculator!")
        break