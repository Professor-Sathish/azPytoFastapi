# Simple Calculator 🧮

A beginner-friendly Python calculator that performs basic math operations.

## What does it do?

This calculator can:
- ➕ Add two numbers
- ➖ Subtract two numbers  
- ✖️ Multiply two numbers
- ➗ Divide two numbers (with safety check for division by zero)

## How to use it

1. Run the program: `python main.py`
2. Enter your first number
3. Enter your second number
4. Choose an operation: `add`, `subtract`, `multiply`, `divide`, or `exit`
5. See your result!
6. Repeat until you type `exit`

## Code Explanation 📚

Let's break down the code line by line:

### Function Definition
```python
def calculator(a, b, operation):
```
- Creates a function named "calculator"
- Takes 3 parameters: `a` (first number), `b` (second number), `operation` (what math to do)

### Addition Operation
```python
if operation == 'add':
    return a + b
```
- If user wants to add, return the sum of a and b

### Subtraction Operation
```python
elif operation == 'subtract':
    return a - b
```
- If user wants to subtract, return a minus b

### Multiplication Operation
```python
elif operation == 'multiply':
    return a * b
```
- If user wants to multiply, return a times b

### Division Operation
```python
elif operation == 'divide':
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
```
- If user wants to divide:
  - First check if b is not zero (can't divide by zero!)
  - If safe, return a divided by b
  - If not safe, return error message

### Unknown Operation
```python
else:
    return "Error: Unknown operation"
```
- If user types something we don't recognize, return error message

### Main Program Loop
```python
while True:
```
- Start an infinite loop that keeps running until user exits

### Getting User Input
```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operation (add, subtract, multiply, divide, exit): ").strip().lower()
```
- Ask user for first number and convert to integer
- Ask user for second number and convert to integer
- Ask user for operation, remove extra spaces with `.strip()`, and make lowercase with `.lower()`

### Exit Condition
```python
if op == "exit":
    break
```
- If user types "exit", break out of the loop and end the program

### Calculate and Display Result
```python
print(calculator(a, b, op))
```
- Call our calculator function with the user's inputs and print the result

## Example Run

```
Enter first number: 10
Enter second number: 5
Enter operation (add, subtract, multiply, divide, exit): add
15

Enter first number: 12
Enter second number: 3
Enter operation (add, subtract, multiply, divide, exit): divide
4.0

Enter first number: 5
Enter second number: 0
Enter operation (add, subtract, multiply, divide, exit): divide
Error: Division by zero

Enter first number: 1
Enter second number: 1
Enter operation (add, subtract, multiply, divide, exit): exit
```

## Key Programming Concepts

- **Functions**: Organizing code into reusable blocks
- **Conditional Statements**: Making decisions with if/elif/else
- **Loops**: Repeating code with while True
- **Input/Output**: Getting user input and displaying results
- **Error Handling**: Preventing crashes with validation
- **String Methods**: Using .strip() and .lower() for input cleaning

Perfect for learning Python basics! 🐍