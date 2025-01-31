def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# TODO
if __name__ == "__main__":
    print("Simple Calculator")
    print("Options: add, subtract, multiply, divide")
    choice = input("Enter Operation: ").lower()
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))


operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}

if choice in operations:
    result = operations[choice](num1, num2)
    print(f"Result: {result}")
else:
    print("Invalid operation")