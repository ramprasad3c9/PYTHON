#TABLES IN BACKWARDS:
a=int(input("enter a number:"))
b=int(input("enter a number:"))
while a>=b:
    i=12
    while i<=12:
        print(a,"X",i,"=",a*i)
        i-=1
        if i==0:
            break
    print()
    a-=1
