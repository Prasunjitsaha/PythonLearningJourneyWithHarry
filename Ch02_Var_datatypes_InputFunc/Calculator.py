a = int(input("Enter the first number: "))
c = input("Enter the operator (+, -, *, /): ")
b = int(input("Enter the second number: "))


if c == '+':
    print("The sum of the numbers is:", a + b)
elif c == '-':
    print("The difference of the numbers is:", a - b)
elif c == '*':
    print("The product of the numbers is:", a * b)
elif c == '/':
    if b != 0:
        print("The quotient of the numbers is:", a / b)
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Invalid operator. Please use +, -, * or /.")


# print("sum of a & b is:", a + b)  # Ensure the output is an integer
# print("subtraction of a & b is:", a - b)  # Ensure the output is an integer
# print("Multiplication of a & b is:", a * b)  # Ensure the output is an integer
# print("Division of a & b is:", a / b)  # Ensure the output is an integer


    

