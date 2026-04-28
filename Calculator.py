import math
import json
import os
from datetime import datetime

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Can't divide by zero")
    return a / b
def power(a, b): return a ** b
def percentage(a, b): return (a * b) / 100
def square_root(a):
    if a < 0:
        raise ValueError("Can't sqrt a negative number")
    return math.sqrt(a)
def logarithm(a):
    if a <= 0:
        raise ValueError("Log only works on positive numbers")
    return math.log(a)
def factorial(a):
    if a < 0 or a != int(a):
        raise ValueError("Factorial needs a non-negative integer")
    return math.factorial(int(a))

HISTORY_FILE = "calc_history.json"
SINGLE_ARG = {"sqrt", "log", "fact"}
VALID_OPS = {"+", "-", "*", "/", "**", "%", "sqrt", "log", "fact"}

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def show_history(history):
    if not history:
        print("No history yet.")
        return
    print("\n--- Last 10 calculations ---")
    for entry in history[-10:]:
        print(f"  {entry['expression']}  [{entry['time']}]")
    print(f"Total: {len(history)} calculations\n")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a valid number, try again.")

def main():
    history = load_history()
    print("=" * 35)
    print("       CALCULATOR")
    print("=" * 35)
    print("Ops: + - * / ** % sqrt log fact")
    print("Type 'h' for history, 'q' to quit")

    while True:
        print()
        op = input("Operation: ").strip().lower()

        if op == "q":
            save_history(history)
            print("History saved. Bye!")
            break
        elif op == "h":
            show_history(history)
            continue
        elif op not in VALID_OPS:
            print("Invalid operation.")
            continue

        a = get_number("First number: ")
        b = None
        if op not in SINGLE_ARG:
            b = get_number("Second number: ")

        try:
            if   op == "+":    result = add(a, b)
            elif op == "-":    result = subtract(a, b)
            elif op == "*":    result = multiply(a, b)
            elif op == "/":    result = divide(a, b)
            elif op == "**":   result = power(a, b)
            elif op == "%":    result = percentage(a, b)
            elif op == "sqrt": result = square_root(a)
            elif op == "log":  result = logarithm(a)
            elif op == "fact": result = factorial(a)

            result = round(result, 10)
            expr = f"{op}({a}) = {result}" if b is None else f"{a} {op} {b} = {result}"
            print(f"Result: {result}")

            history.append({
                "expression": expr,
                "time": datetime.now().strftime("%H:%M:%S")
            })

        except (ValueError, OverflowError) as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
