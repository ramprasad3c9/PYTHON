#tables in backwards in 1 to 5:
a=int(input("enter a number:"))
b=int(input("enter a number:"))
while b>=a:
    i=12
    while i>=1:
        print(b,"X",i,"=",b*1)
        i-=1
    print()
    b-=1
