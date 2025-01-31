def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Dictionary of operations (global for reusability)
OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}

def calculate():
    """Handles user input and performs calculations based on user choice."""
    print("\n🔢 Simple Calculator")
    print("Options: add, subtract, multiply, divide")

    choice = input("Enter operation: ").strip().lower()
    
    if choice not in OPERATIONS:
        print("❌ Invalid operation. Please choose a valid option.")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = OPERATIONS[choice](num1, num2)
        print(f"✅ Result: {result:.2f}")
    except ValueError as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    calculate()
