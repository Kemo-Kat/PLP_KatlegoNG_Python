
num1 = float(input("First number:"))
num2 = float(input("Second number:"))
operator = input("Operator:")

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Number cannot be divided by ZERO!!")
else:
    print("Invalid operation. Please enter +, -, *, or /.")



