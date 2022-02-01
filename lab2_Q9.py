
q1 = tuple((input("enter your name : ")))
q2 = input("enter a letter of your name : ")
if q2 in q1:
    result = q1.index(q2)
    print("the index value of ",q2," of your name is :",result)

else :
    print("index value not found")
