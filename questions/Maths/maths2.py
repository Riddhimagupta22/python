# To find the factors of number

print("To find the factors of number")

def factor_of_num(number):
     
     print (f"The factors of {number} is :-",end=" ")
     for i in range( 1, number + 1):
            if number % i == 0 :
               print ( i,end = " ")
     print ()         

number = int(input("Enter a number :-"))
factor_of_num(number)  
           
# HCF 
print ("To find HCF")
def hcf(num1,num2):
     
     if num1>num2:
           smaller = num2
     else: 
           smaller = num1 
     
     for num in range( 1 , smaller + 1):
          if ( num1 % num == 0 and num2 % num ==0):
               result = num
     return result

number1 = int(input("Enter first number :-"))
number2 = int(input("Enter second number :-"))

hcf_result = hcf(number1,number2)

print(f"HCF of {number1} and {number2} is:-{hcf_result}")
print()



# Armstrong  number in an interval
print("To check Armstrong  number in an interval")

def armStrong(num):
   number = str(num)
   num_len = len(number)
   total = sum(int(digit)** num_len for digit in number)

   return total == num
def armStrong_interval(start,end):
    armStrong_num = []

    for num in range (start,end + 1):
        if armStrong (num):
            armStrong_num.append(num)
    return armStrong_num    

Starting_Number = int(input("Enter Starting number: "))
Ending_Number = int(input("Enter Ending number: "))

armStrong_number = armStrong_interval(Starting_Number,Ending_Number)

print(f"Armstrong number between {Starting_Number} and {Ending_Number} is :- {armStrong_number}")
print()    

# Armstrong 
print("To check Armstrong  number ")
def armStrong(num):
    number = str(num)
    num_len = len(number)
    total = 0

    for digit in number:
        total += int(digit) ** num_len
    return total == num
Number = int(input("Enter a number: "))
if armStrong(Number):
    print(f"{Number} is an Armstrong number.")
else:
    print(f"{Number} is not an Armstrong number.")
print()    

#Prime Number in interval 
print("To check is a number prime ")
Upper_Number = int(input("Enter Upper number:-")) 
lower_Number = int(input("Enter Lower number:-"))


if lower_Number == 1:
    print(f"{lower_Number} is not prime number")

for num in range(lower_Number,Upper_Number+1):
   if num > 1 :    
        for i in range (2,num):
          if num % i == 0 :
                print(f"{num} is not prime number")
                break
   else : 
               print(f"{num} is prime number")   
print()
