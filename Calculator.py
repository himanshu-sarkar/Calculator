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


print("Simple Calculator")

while True:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (+ - * /): ")

    if op == "+":
        print("Result:", add(a, b))
    elif op == "-":
        print("Result:", subtract(a, b))
    elif op == "*":
        print("Result:", multiply(a, b))
    elif op == "/":
        print("Result:", divide(a, b))
    else:
        print("Invalid operation")

    again = input("Do you want to continue? (y/n): ")
    if again.lower() != "y":
        print("Goodbye!")
        break
