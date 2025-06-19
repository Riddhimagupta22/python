# Calculator

print("To make simple calculator\n")

num1 = float(input("Enter first number :-"))
num2 = float(input("Enter second number :-"))

print("Please select operation:-\n","1) Addition\n","2) Subtraction\n","3) Multiplication\n","4) Division\n")

choice = int(input("Select operation (1-4) :-\n"))

if choice == 1 :
    sum = num1 + num2
    print(f"{num1} + {num2} = {sum} ")
elif choice == 2 :
    sub = num1 - num2
    print(f"{num1} - {num2} = {sub} ")
elif choice == 3 :
    multiply = num1 + num2
    print(f"{num1} * {num2} = {multiply} ")
elif choice == 4 :
    divide = num1 + num2
    print(f"{num1} / {num2} = {divide} ")
else:
    print("Enter a valid number")    