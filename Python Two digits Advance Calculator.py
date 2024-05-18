#Python Two digits Advance Calculator
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter the operator (add/sub/mul/div): ")


# Perform operation based on user's choice
if operator == 'add':
    result = num1 + num2
    print("The result is: ", result)
elif operator == 'sub':
    result = num1 - num2
    print("The result is: ", result)
elif operator == 'mul':
    result = num1 * num2
    print("The result is: ", result)
elif operator == 'div':
    if num2 != 0:
        result = num1 / num2
        print("The result is: ", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator! Please enter add/sub/mul/div only")
print("This program is created by Muhammad hamza ")