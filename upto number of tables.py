#write a python program print the multiplication tables of all numbers up to 12 in a given using while loop
a=int(input("enter a number:"))
b=int(input("enter a number:"))
while (a<=b):
    i=1
    while i<=12:
        print(a,"X",i,"=",a*i)
        i+=1
    print()
    a+=1
