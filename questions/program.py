# Hello Word
print("Hello World")
print()

# Swap of two variable
print("Swap two variable")

Number1 = input("Enter First number:-")
Number2= input("Enter Second number:-")

Number1,Number2 = Number2,Number1

print ("The value of Number1 is :-",Number1)
print ("The value of Number2 is :-",Number2)
print()

# Leap Year 
print("To check a leap year")
year = int(input("Enter a year:-"))
if(year% 100 ==0 and year % 400 == 0):
    print(f"{year} is a leap year")
elif(year% 4 ==0 and year % 100 != 0):
 print(f"{year} is a leap year")   
else: 
    print(f"{year} is a non leap year")  
    print() 