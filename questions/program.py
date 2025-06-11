# Hello Word
print("Hello World")
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