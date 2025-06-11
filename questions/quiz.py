questions = ["Which language was used to create facebook?","Python","French","JavaScript","Ruby"],
["Which language was used to create facebook?","Python","French","JavaScript","Ruby"],
["Which language was used to create facebook?","Python","French","JavaScript","Ruby"],
["Which language was used to create facebook?","Python","French","JavaScript","Ruby"]

level =[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]

i=0
for i in range(0,len(questions)):
    questions = questions[i]
    print(f"Question for Rs.{level[i]}")
    print(f"a.{questions[1]} b.{questions[2]}")
    print(f"c.{questions[3]} d.{questions[4]}")

    reply = str(input("Enter Your Answer:-"))

    if(reply == questions[-1]):
        print(f"Correct answer,You have won{level[i]}")

    else:
        print(f"You losse")

