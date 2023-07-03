num1 = float(input("Please enter the first number:"))
num2 = float(input("Please enter the second number:"))

operator = str(input("Please enter Operator:"))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
else:
    print("Invalid")
    