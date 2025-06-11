'''i = 50
while i:
    print("Hi",i)
    i+=1 
    if i == 90:
       break 

# function 

def comparsion(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater")

def sum_num(a,b):
    sum = a+b 
    print("Sum of",a,"and",b,"is",sum)       

num1 = int(input("Enter First number:-")) 
num2 = int(input("Enter Second number:-"))

sum_num(num1,num2)

comparsion(num1,num2)
'''
# f string
name = input("Enter Your name:-")
place = input("Enter Your place:-")


print(f"My name is {name}. I belong to {place}")

print(type(f"{2*50}"))



