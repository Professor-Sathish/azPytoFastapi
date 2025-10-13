while True:
    num1=int(input("Enter a number 1: "))

    num2=int(input("Enter a number 2: "))

    choose=int(input("Enter your choice 1.Add 2.Subtract 3.Multiply 4.Divide 5.Exit: "))

    if choose == 1:
        print(f"The sum is: {num1 + num2}")
    elif choose == 2:
        print(f"The difference is: {num1 - num2}")
    elif choose == 3:
        print(f"The product is: {num1 * num2}")
    elif choose == 4:
        print(f"The quotient is: {num1 / num2:.3f}")
    elif choose == 5:
        print("Exiting the program.")
        break
    else :
        print("Invalid choice")