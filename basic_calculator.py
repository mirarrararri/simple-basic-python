#Input - ask user to enter first and second number
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#Process 
sol = input("Choose Operator (+, -, *, /): ")

if sol == "+":
    print(f"{num1} + {num2} = ",num1 + num2)
elif sol == "-":
    print(f"{num1} - {num2} = ",num1 - num2)
elif sol == "*":
    print(f"{num1} * {num2} = ",num1 * num2)
elif sol == "/":
    if num2 != 0:
        print(f"{num1} / {num2} = ",num1 / num2)
    else:
        print("Error: Division by zero")

#Output -print
else:
    print("Invalid Operator")

    



