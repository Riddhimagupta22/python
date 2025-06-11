#Prime Number in interval 

print("To check is a number prime ")
Upper_Number = int(input("Enter Upper number:-")) 
lower_Number = int(input("Enter Lower number:-")) 


if lower_Number == 1:
    print(f"{lower_Number} is not prime number")

if lower_Number > 1 :    
        for i in range (2,Upper_Number):
          if Upper_Number % i == 0 :
                print(f"{Number} is not prime number")
                break
        else : 
               print(f"{Number} is prime number")   
print()




# ArmStrong
def armStrong(num):
     number = num
     num_len = len(num)
