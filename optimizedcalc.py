import os
def add(a, b):
        return a + b

def subtract(a, b):
        return a - b

def multiply(a, b):
        return a * b
def divide(a, b):
    if b != 0:
         return a / b
    else:
        print("error: division by zero")
        return None
operation_dict={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print("welcome to optimized calculator")
calcActive = True
while calcActive:
    
    num1 = int(input("enter the first number: "))
    for symbol in operation_dict:
        print(symbol)
    operator = input("enter the operator :")
    num2 = int(input("enter the second number: "))
    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = subtract(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)
    else:
        print("invalid operator")
        result = None
    again= input(f"do you want to perform another calculation with {result}? press n, if you want to start a new calculation press n and if you want t0 exit presss x:  ")
    if again.lower() == "n":
        choice=input("what operation do you want to perform with the result? (+, -, *, /): ")
        if choice == "+":
            num3 = int(input("enter the number to add: "))
            result = add(result, num3)
        elif choice == "-":
            num3 = int(input("enter the number to subtract: "))
            result = subtract(result, num3)
        elif choice == "*":
            num3 = int(input("enter the number to multiply: "))
            result = multiply(result, num3)
        elif choice == "/":
            num3 = int(input("enter the number to divide: "))
            result = divide(result, num3)
        else:
            print("invalid operator")
    elif again.lower() == "n":
        pass
    #remember what pass does: it is a placeholder that does nothing, it is used when you want to write code later but you don't want to leave the block empty
    