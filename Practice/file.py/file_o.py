count = 0
with open("Practice/file.py/practice.txt", "r") as f:
    data = f.read()
    print(data)

    num = data.split(",")
    for value in num:
        if (int(value) % 2 == 0):
            count += 1
            print(f"{value}")

        else:
            pass  
    print (f"There are {count} even number.")      


