try:
    num1 = int(input("Enter first integer: "))
    num2 = int(input("Enter second integer: "))
    result = num1 / num2
    print("Division result:", result)
except ValueError:
    print("Invalid input! Please enter numbers only.")
except ZeroDivisionError:
    print("Error! Cannot divide by zero.")
