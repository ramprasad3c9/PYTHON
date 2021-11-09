#PRINT EVEN NUMBERS:
a=int(input("enter a begining number:"))
b=int(input("enter a end number:"))
while a<=b:
    if a%2==0:
        print(a,end=',')
    a+=1
