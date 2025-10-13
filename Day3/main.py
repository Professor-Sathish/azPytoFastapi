def calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Unknown operation"
# Example usage:
while True:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    op = input("Enter operation (add, subtract, multiply, divide, exit): ").strip().lower()
    if op == "exit":
        break
    print(calculator(a, b, op))