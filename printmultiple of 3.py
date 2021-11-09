#PRINT MULTIPLES OF 3:
a=int(input("enter a begining number:"))
b=int(input("enter a end number:"))
while a<=b:
    if a%3==0:
        print(a,end=",")
    a+=1
