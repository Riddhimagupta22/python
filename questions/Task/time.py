import time
name= str(input("Enter Your Name:"))
t= time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
print(hour)

if(hour>=0 and hour<=12):
    print("Good Morning!",name)
elif(hour>=12 and hour<=15):
  print("Good Afternoon!",name)
elif(hour>=15 and hour<=19):
  print("Good Evening!",name)
elif(hour>=19 and hour<=0):
  print("Good Night!",name)
else:
   print("Enter valid Time")
