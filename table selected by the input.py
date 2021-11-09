#program should ask me like this
#1 table up to 3
#2 table up to 2
#3 table up to 4
a=int(input("enter a begining table:"))
b=int(input("enter a ending table:"))
while a<=b:
    i=1
    r=int(input("table up to:"))
    while i<=r:
        print(a,"X",i,"=",a*i)
        i+=1
    print()
    a+=1
