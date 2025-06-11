marks = [1,2,3,4,10,5,6,7,8,9,10] 
colors = ["pink","red","purple"]

clas = [i*i for i in range(5)]
print(clas)
print(marks+ clas)
print(marks)
print(type(marks))
print(marks[1])
print(marks[-1])
print(marks[0:5])
print(marks[len(marks)-1]) # postive index
print(len(marks))
# 
print(marks[1:4:2])
# 
if "ridd" in marks:
    print(True)
else:
    print(False)

if "d" in "ridd":
    print(True)
else:
    print(False)      

marks.append(11,)
marks.sort()
marks.sort(reverse=True)
marks.reverse()
marks.remove(9)
marks.pop(4)
marks.insert(4,100)
marks.extend(colors)
print(marks.index(4))
marks.clear()
print(marks)
print(marks.count(10))
























