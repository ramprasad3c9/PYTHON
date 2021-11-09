#TOTAL,PERCENTAGE,DIVISION:
number=int(input("enter roll number:"))
a=int(input("enter physics marks:"))
b=int(input("enter chemistry marks:"))
c=int(input("enter computer science marks:"))
print("Roll number:",number)
print("marks in physics:",a)
print("marks in chemistry:",b)
print("marks in computer science:",c)
total=a+b+c
print("total marks:",total)
percentage=(total/3)
print("the percentage is:",percentage,"%")
if percentage<=80:
    print("first")
elif 70<=percentage>=79:
    print("second")
elif 60<=percentage>=69:
    print("third")
elif 50<=percentage>=59:
    print("fourth")
else:
    print("fail")
