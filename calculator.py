#functions to consider: 1. addition 2. subtraction 3. multiplication 4. division 5. factorial 
def addition(*numbers):
    total=0
    for num in numbers:
        total+=num
    return total
def subtraction(*numbers):
    total=numbers[0]
    for num in numbers[1:]:
        total-=num
    return total
def multiply(*numbers):
    total=1
    for num in numbers:
        total*=num
    return total
def division(*numbers):
    total=numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "Error: Division by zero is not allowed."
        total/=num
    return total
def factorial(n):
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        total=1
        for i in range(2, n + 1):
            total *= i
        return total

print("welcome to my calculator")
operation= input("choose an operation: \n 1. addition \n 2. subtraction \n 3. multiplication \n 4. division \n 5. factorial: ")
if operation == "1":
    numbers= input("enter numbers to add, separated by spaces: ")
    num_list= [float(num) for num in numbers.split()]
    result= addition(*num_list)
    print(f"The result of addition is: {result}")
elif operation == "2":
    numbers= input("enter numbers to subtract, separated by spaces: ")
    num_list= [float(num) for num in numbers.split()]
    result= subtraction(*num_list)
    print(f"The result of subtraction is: {result}")
elif operation == "3":
    numbers= input("enter numbers to multiply, separated by spaces: ")
    num_list= [float(num) for num in numbers.split()]
    result= multiply(*num_list)
    print(f"The result of multiplication is: {result}")
elif operation == "4":
    numbers= input("enter numbers to divide, separated by spaces: ")
    num_list= [float(num) for num in numbers.split()]
    result= division(*num_list)
    print(f"The result of division is: {result}")
elif operation == "5":
    number= int(input("enter a number to find its factorial: "))
    result= factorial(number)
    print(f"The factorial of {number} is: {result}")
else:
    print("Invalid operation selected. Please choose a number between 1 and 5.")
