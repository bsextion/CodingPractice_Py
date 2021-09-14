# num1  = input("What is your first number?: ")
# num2  = input("What is your second number?: ")
# result = int(num1) + int(num2)
# print(result)

# result = int(num1) + int(num2)


num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
     print(num1 / num2)  
elif op == "*":
     print(num1 * num2)
else:
    print("Invalid operator")


