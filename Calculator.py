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

    if op == "+":
        print("Result:", add(a, b))
    elif op == "-":
        print("Result:", subtract(a, b))
    elif op == "*":
        print("Result:", multiply(a, b))
    elif op == "/":
        print("Result:", divide(a, b))
    elif op == "**":
        print("Result:", power(a, b))
    else:
        print("Invalid operation")

    print("-" * 35)

    again = input("Do you want to continue? (y/n): ")
    if again.lower() != "y":
        print("\nThank you for using the calculator!")
        break