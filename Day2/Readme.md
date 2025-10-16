Day 2:

Today we are going to learn about Looping in python .

In this we contains Looping constraint additionaly were there will be a repitation untill the condition get false

## Line-by-line explanation of main.py

- `while True:`  
  Starts an infinite loop so the program keeps running until explicitly stopped.

- `num1 = int(input("Enter a number 1: "))`  
  Prompts the user for the first number, converts the input string to an integer, and stores it in `num1`.

- `num2 = int(input("Enter a number 2: "))`  
  Prompts the user for the second number, converts it to an integer, and stores it in `num2`.

- `choose = int(input("Enter your choice 1.Add 2.Subtract 3.Multiply 4.Divide 5.Exit: "))`  
  Asks the user to pick an operation by number (1–5), converts the input to an integer, and stores it in `choose`.

- `if choose == 1:`  
  Checks if the user chose addition.  
  `print(f"The sum is: {num1 + num2}")`  
  Calculates `num1 + num2` and prints the result using an f-string.

- `elif choose == 2:`  
  Checks if the user chose subtraction.  
  `print(f"The difference is: {num1 - num2}")`  
  Calculates `num1 - num2` and prints the result.

- `elif choose == 3:`  
  Checks if the user chose multiplication.  
  `print(f"The product is: {num1 * num2}")`  
  Calculates `num1 * num2` and prints the result.

- `elif choose == 4:`  
  Checks if the user chose division.  
  `print(f"The quotient is: {num1 / num2:.3f}")`  
  Divides `num1` by `num2` and prints the result rounded to 3 decimal places.  
  Note: If `num2` is 0, Python raises a ZeroDivisionError (no guard is present here).

- `elif choose == 5:`  
  Checks if the user chose to exit.  
  `print("Exiting the program.")`  
  Prints a message.  
  `break`  
  Breaks out of the loop, ending the program.

- `else:`  
  Handles any invalid choice outside 1–5.  
  `print("Invalid choice")`  
  Shows an error message and loops again.

### Flow summary
1. Read two numbers.
2. Read the operation choice (1–5).
3. Perform the selected operation and print the result.
4. Repeat until the user selects 5 (Exit).