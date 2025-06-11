# conversion 
print("Conversion Celsius to Fahrenheit")
temp= float(input("Enter a temp(in Celsius):-"))
Fahrenheit = (temp*9/5) + 32
print(f"Kilometre to Miles of {temp} km is:-",Fahrenheit,"fahrenheit")
print()

# Prime number 
print("To check is a number prime ")
Number = int(input("Enter a number:-")) 

if Number == 1:
    print(f"{Number} is not prime number")

if Number > 1 :    
        for i in range (2,Number):
          if Number % i == 0 :
                print(f"{Number} is not prime number")
                break
        else : 
               print(f"{Number} is prime number")   
print()

# lagrest number
print("The largest among 3 numbers ")
Number1 = float(input("Enter First number:-")) 
Number2= float(input("Enter Second number:-"))
Number3 = float(input("Enter Third number:-")) 

if(Number1 > Number2 and Number1 > Number3 ):
    print(f"{Number1} is largest among 3 numbers")
elif(Number2 > Number3 and Number2 > Number1 ):
    print(f"{Number2} is largest among 3 numbers")
elif(Number3 > Number1 and Number3 > Number2 ):
    print(f"{Number3} is largest among 3 numbers")
else:
    print("Enter a valid number") 

print()

# Positive or Negative 
print("To Check a number Postive or Negative ")
Number = float(input("Enter a number:-")) 
if (Number >= 0):
    print(f"{Number} is a positive number")
else:  
    print(f"{Number} is a negative number")  
print()

# Odd/ Even 
print("To Check a number is Odd or Even ")
Number = int(input("Enter a number:-")) 

if (Number %2 == 0):
    print(f"{Number} is an even number")
else:  
    print(f"{Number} is an odd number")  
print()

# Sum of Natural Number 
print("Sum of Natural Number ")
number = int(input("Enter a number:-")) 
if number < 0 :
    print("Enter a Postive Number")
else:
    sum = 0
    for i in range(1,number+1):
      sum += i  
print(f"Sum of {number} natural number is:-",sum)
print()

# Multiplication 
print("Multiplication Table ")
number = int(input("Enter a number:-"))
num = int(input("Enter a number:-"))
for i in range(num):
    result = number * i
    print(f"{number} * {i} = {result}")
print()

# conversion 
print("Conversion kilometers to miles ")
number = float(input("Enter a number(in kilometers):-"))
miles = number*0.621371
print(f"Kilometre to Miles of {number} km is:-",miles,"miles")
print()
    
#Area
print("Area of Triangle ")
def area_of_triangle(base,height):
    Area_of_Triangle = 0.5*base*height
    print(f"Area of Triangle is:- ",Area_of_Triangle)

Base = float(input("Enter Base:-"))
Height = float(input("Enter Height:-"))
area_of_triangle(Base,Height)
print()


# Square Root
print("Square Root of a Number ")
def square_root(num):
    squareRoot = num*num
    print(f"Square Root of {num} is:-",squareRoot)

number = int(input("Enter a number:-"))
square_root(number)
print()


# Add
print("Addition of 2 Number ")
def add(a,b,):
    sum = a+b 
    print(f"Sum of {a} and {b} :-",sum)

num1 = int(input("Enter First number:-"))
num2 = int(input("Enter Second number:-"))

add(num1,num2)
print()

# factorial
print("Factorial of a Number ")
def factorial(num):
    if(num == 1 or num ==0):
        return 1
    else:
        return(num*factorial(num-1))
    

number = int(input("Enter the number:-"))
print(f"The Factorial of {number} is :-",factorial(number))
print()


# fibonacci
print("Fibonacci of a Number ")
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

number = int(input("Enter the Number:-"))
for i in range(number):
    print(fibonacci(i),end=" ")
print()











